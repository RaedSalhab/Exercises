"""R-3.2 The number of operations executed by algorithms A and B is 8n log n and
2n 2 , respectively. Determine n 0 such that A is better than B for n ≥ n 0 ."""

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,1.5,100)
plt.plot(n, 8*n*np.log2(n), label='8nlog2(n)')
plt.plot(n, 2*n**2, label='2*n**2')
plt.xlabel('n label')
plt.ylabel('f(n) label')
plt.title("R-3.2 Plot")
plt.legend(loc='upper left')
plt.grid()
plt.show()

# Solution is n0 = 1.241