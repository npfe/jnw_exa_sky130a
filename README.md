
[![GDS](../../actions/workflows/gds.yaml/badge.svg)](../../actions/workflows/gds.yaml)
[![DRC](../../actions/workflows/drc.yaml/badge.svg)](../../actions/workflows/drc.yaml)
[![LVS](../../actions/workflows/lvs.yaml/badge.svg)](../../actions/workflows/lvs.yaml)
[![DOCS](../../actions/workflows/docs.yaml/badge.svg)](../../actions/workflows/docs.yaml)
[![SIM](../../actions/workflows/sim.yaml/badge.svg)](../../actions/workflows/sim.yaml)

# Who
nicolas

# Why

Test current mirror with a cascode configuration and observe stability of the circuit.

# How

sky130a pdk, xschem for schematic, magic vlsi for layout, ngspice for simulations. CICSIM and Python for ploting.p

# What

| What            |        Cell/Name |
| :-              |  :-:       |
| Schematic       | design/JNW_EXA_SKY130A/JNW_EXA.sch |
| Layout          | design/JNW_EXA_SKY130A/JNW_EXA.mag |


# Changelog/Plan

| Version | Status | Comment|
| :---| :---| :---|
|0.1.0 | :X: | Using JNWATR_NCH_2C5F0 NFET |
|0.2.0 | :X: | Using JNWATR_NCH_2C5F0 NFET |

# Signal interface

| Signal       | Direction | Domain  | Description           |
| :---         | :---:     | :---:   | :---:                 |
| IBP          | Input     | 1.95V   | Current mirror input  |
| IBN          | Output    | 1.95V   | Current mirror output |
| VSS          | Input     | Ground  |                       |


# Key parameters

| Parameter           | Min     | Typ           | Max     | Unit  |
| :---                | :---:     | :---:           | :---:     | :---: |
| Technology          |         | Skywater 130 nm |         |       |
| AVDD                | 1.7    | 1.8           | 1.9    | V     |
| Temperature         | -40     | 27            | 125     | C     |
