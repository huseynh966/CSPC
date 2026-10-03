"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# 1. читаем данные
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# 2. аналитический закон
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# 3. два графика с общими осями
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed)
ax1.set_title("Observed data")
ax1.set_xlabel("time")
ax1.set_ylabel("count")

ax2.plot(t, analytical)
ax2.set_title("Analytical: N0 * exp(-lambda * t)")
ax2.set_xlabel("time")

# 4. сохраняем
plt.tight_layout()
plt.savefig("figure.png")
