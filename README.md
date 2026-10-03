# CSPC

## PW1 --- Lab B

**What the data showed:** the observed count decreases exponentially with time, from 5000 at t = 0, falling quickly at first and then more slowly.

**Comparison with the analytical law:** the observed points follow the analytical curve N0·exp(-0.3t) closely, with absolutely minimal scatter as the points completely match the graph line, so the data match the decay law.

**Pipeline:** the Snakemake rule rebuilds figure.png from decay_observed.csv by running plot.py, and does nothing if the input has not changed.
