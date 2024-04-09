import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Generate data
n = 100
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)

# Perform Lowess smoothing (frac controls the smoothness of the line)
y_est = lowess(y, x,frac=0.2)

# Plot results
plt.plot(x, y, "r.", x, y_est[:,1], "b-")
plt.show()