"""P-3.55 Perform an experimental analysis of the three algorithms preﬁx average1,
preﬁx average2, and preﬁx average3, from Section 3.3.3. Visualize their
running times as a function of the input size with a log-log chart."""

from cProfile import label
import matplotlib.pyplot as plt
from matplotlib import scale
import numpy as np

n = np.linspace(0, 10000, 10000)
plt.plot(n, n**2, label='preﬁx_average 1 and 2')
plt.plot(n, n, label='preﬁx_average 3')
plt.xlabel('n label')
plt.ylabel('f(n) label')
plt.xscale('log')
plt.yscale('log')
plt.title("P-3.55 Plot")
plt.legend(loc='upper left')
plt.grid()
plt.show()