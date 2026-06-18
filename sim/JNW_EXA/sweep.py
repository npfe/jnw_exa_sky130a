#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yaml, re, sys
from pathlib import Path
from datetime import datetime


def main(name):
  # Delete next line if you want to use python post processing
  return
  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  import cicsim as cs
  fname = name +".png"

  print(f"Saving {fname}")
  cs.rawplot(name + ".raw", "v(v-sweep)", "i(v0)" , ptype="", fname=fname)

  # Save new yaml file
  with open(yamlfile,"w") as fo:
    yaml.dump(obj,fo)

if __name__ == "__main__":
    try:
        from cicsim.ngraw import toDataFrame
    except ImportError:
        from cicsim.ngraw import ngRawRead

        def toDataFrame(raw_path):
            arrs, plots = ngRawRead(raw_path)
            if not arrs or not plots:
                return None
            return pd.DataFrame(data=arrs[0], columns=plots[0]["varnames"])
    
    RAW_DIR = Path(r"./output_sweep")
    RAW_TOKEN = "SchGtKttmmTtVt"
    X_COL = "v(v-seep)"
    COMPLEX_MODE = "real"
    SIGNALS_TO_KEEP = None
    SIGNAL_NAME = 'i_out'
    X_MIN_DIST = 0.8

    # Save outputs
    CSV_OUT = "all_raw_data_long.csv"
    PARQUET_OUT = "all_raw_data_long.parquet"

    def simplify_complex(series: pd.Series, mode: str = "real") -> pd.Series:
        """Convert complex-valued traces into a plottable real series."""
        if np.iscomplexobj(series):
            if mode == "imag":
                return np.imag(series)
            elif mode == "abs":
                return np.abs(series)
            return np.real(series)
        return series


    def auto_pick_x_col(df: pd.DataFrame) -> str:
        """Try to find a sensible common x-axis column in volts."""
        if X_COL and X_COL in df.columns:
            return X_COL

        candidates = list(df.columns)

        # Strong hints first
        preferred_patterns = [
            r"^v\(.*sweep.*\)$",
            r"^v\(.*in.*\)$",
            r"^v\(.*bias.*\)$",
            r"^v\(.*\)$",
            r".*volt.*",
            r".*sweep.*",
        ]

        for pat in preferred_patterns:
            for col in candidates:
                if re.match(pat, str(col).strip().lower()):
                    return col

        # Fall back to first column if nothing better exists
        return candidates[0]


    def pick_y_cols(df: pd.DataFrame, x_col: str):
        cols = [c for c in df.columns if c != x_col]
        if SIGNALS_TO_KEEP:
            cols = [c for c in cols if c in SIGNALS_TO_KEEP]
        return cols


    all_frames = []
    raw_files = sorted(RAW_DIR.glob(f"*{RAW_TOKEN}*.raw"))

    if not raw_files:
        raise FileNotFoundError(f"No .raw files found under: {RAW_DIR}")

    print(f"Found {len(raw_files)} raw files")

    for raw_file in raw_files:
        print(f"Reading: {raw_file}")
        df = toDataFrame(str(raw_file))

        if df is None or df.empty:
            print(f"  Skipping empty/unreadable file: {raw_file.name}")
            continue

        x_col = auto_pick_x_col(df)
        y_cols = pick_y_cols(df, x_col)

        if not y_cols:
            print(f"  No plottable y-columns found in: {raw_file.name}")
            continue

        temp = df[[x_col] + y_cols].copy()

        # Standardise axis naming
        temp = temp.rename(columns={x_col: "x_V"})
        temp["x_V"] = simplify_complex(temp["x_V"], COMPLEX_MODE)

        # Convert to long format: one row per (file, x, signal)
        long_df = temp.melt(
            id_vars=["x_V"],
            value_vars=y_cols,
            var_name="signal",
            value_name="y"
        )

        long_df["y"] = simplify_complex(long_df["y"], COMPLEX_MODE)

        long_df["y"] = -1 * long_df["y"]
        long_df["y"] = long_df["y"] / 1e-6

        long_df.insert(0, "file", raw_file.name)
        long_df.insert(1, "file_path", str(raw_file))

        all_frames.append(long_df)

    if not all_frames:
        raise RuntimeError("No usable data could be extracted from the .raw files.")

    all_data = pd.concat(all_frames, ignore_index=True)

    # Optional: sort nicely
    all_data = all_data.sort_values(["signal", "file", "x_V"]).reset_index(drop=True)
    all_data = all_data[all_data["signal"].isin(["v(v-sweep)", "i(v0)"])]
    
    # Save combined data
    #all_data.to_csv(CSV_OUT, index=False)
    #all_data.to_parquet(PARQUET_OUT, index=False)

    dist_df = all_data[all_data["x_V"] >= X_MIN_DIST].copy()

    # =========================
    # PLOTTING
    # =========================
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{SIGNAL_NAME}_{timestamp}")

    print(f"Plotting distribution")
    plt.figure(figsize=(8, 5))
    plt.hist(dist_df["y"], bins=50, edgecolor="black", alpha=0.75)
    plt.xlabel("y [µA]")
    plt.ylabel("Count")
    plt.title("Distribution of Iout for Vout ≥ 0.4 V")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"media/plot_{safe_name}_dist.png", dpi=150)


    # One figure per signal; one line per file
    for signal_name, signal_df in all_data.groupby("signal", sort=True):
        print(f"Plotting signal {signal_name}")
        fig, ax = plt.subplots(figsize=(12, 8))

        for file_name, file_df in signal_df.groupby("file", sort=True):
            ax.plot(file_df["x_V"], file_df["y"], label=file_name, linewidth=1.0)

        ax.set_xlabel("Voltage [V]")
        ax.set_ylabel(f"{signal_name} [µA]")
        ax.set_title(f"{signal_name} vs Voltage")
        ax.grid(True, alpha=0.3)

        ax.legend(
            loc="center left",
            bbox_to_anchor=(1.02, 0.5),
            fontsize=7,
            ncol=1,
            frameon=False
        )

        fig.tight_layout()
    plt.savefig(f"media/plot_{safe_name}.png", dpi=150)


    stats = dist_df["y"].describe(percentiles=[0.01, 0.05, 0.5, 0.95, 0.99])

    # Convert to rows
    stats_rows = [(idx, f"{val:.6g}") for idx, val in stats.items()]

    def ascii_table(headers, rows):
        # Compute column widths
        widths = [len(str(h)) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))

        def hline():
            return "|" + "|".join("-" * (w + 2) for w in widths) + "|"

        def fmt_row(row):
            return "| " + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |"

        lines = []
        lines.append(fmt_row(headers))
        lines.append(hline())
        for row in rows:
            lines.append(fmt_row(row))
        return "\n".join(lines)

    table_txt = ascii_table(
        headers=("metric", "value"),
        rows=stats_rows
    )

    stats_txt_path = f"media/global_stats_x_ge_{str(X_MIN_DIST).replace('.', 'p')}_{timestamp}.txt"

    with open(stats_txt_path, "w", encoding="utf-8") as f:
        f.write(f"Global distribution statistics\n")
        f.write(f"Condition: x_V >= {X_MIN_DIST} V\n\n")
        f.write(table_txt)
        f.write("\n")

    print(table_txt)

