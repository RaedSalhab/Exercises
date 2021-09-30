"""R-3.1 Graph the functions 8n, 4n log n, 2n 2 , n 3 , and 2 n using a logarithmic scale
for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
point with x-coordinate at log n and y-coordinate at log y."""

from cProfile import label
from tkinter import N
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0, 10, 50)
fig, ax = plt.subplots()
plt.plot(n, 8 * n, label='linear') 
plt.plot(n, 4 * n * np.log2(n), label='n log n') 
plt.plot(n, 2*n**2, label='quadratic')
plt.plot(n, n**3, label='cubic')
plt.plot(n, 2**n, label='exponential')
plt.xlabel('n label')
plt.ylabel('f(n) label')
plt.title("R-3.1 Plot")
plt.legend(loc='upper left')
plt.show()
