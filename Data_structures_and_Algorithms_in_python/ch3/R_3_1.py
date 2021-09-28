from cProfile import label
from tkinter import N
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0, 10, 50)
fig, ax = plt.subplots()
plt.plot(n, 8 * n, label='linear') 
plt.plot(n, 4 * n * np.log(n), label='n log n') 
plt.plot(n, 2*n**2, label='quadratic')
plt.plot(n, n**3, label='cubic')
plt.plot(n, 2**n, label='exponential')
plt.xlabel('n label')
plt.ylabel('f(n) label')
plt.title("R-3.1 Plot")
plt.show()
