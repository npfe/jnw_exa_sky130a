### Cascode current mirror investigations.

#### Specification

| Parameter | Value | Unit | 
| --------- | ----- | ---- | 
| I<sub>in</sub> | 20 | uA |
| I<sub>out</sub> | 20 | uA |
| V<sub>out</sub> | 0 - 1.95 | V |
| Accuracy V<sub>out</sub>=0.8-1.95  | 1  | %    |


Using transistors `JNWATR_NCH_12CF0` with a channel length of `6um`.

Sweeping V<sub>out</sub> from 0 to 1.95V current matching looks like this:


Sweeping V<sub>out</sub> from 0 to 1.95V current matching looks like this:
![Iout vs Vout](../../sim/JNW_EXA/media/plot_i_out_20260617_215852.png)

![Iout distribution](../../sim/JNW_EXA/media/plot_i_out_20260617_215852_dist.png)

Global distribution statistics
Condition: x_V >= 0.4 V


| metric | value    |
|--------|----------|
| count  | 3480     |
| mean   | 20.3028  |
| std    | 0.461958 |
| min    | 18.9824  |
| 1%     | 19.1349  |
| 5%     | 19.4998  |
| 50%    | 20.3186  |
| 95%    | 21.0011  |
| 99%    | 21.3982  |
| max    | 21.6214  |


Simulation parameters: `mc 30 loops` - see [sweep.spi](../../sim/JNW_EXA/sweep.spi),

