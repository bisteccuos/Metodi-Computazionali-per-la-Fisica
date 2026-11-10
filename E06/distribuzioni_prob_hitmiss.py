import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms

# HIT/MISS
def parabola(n):
    x = np.random.uniform(0,10,n)
    y = np.random.uniform(0,0.3,n) # 0.3 è il massimo della funzione 3/1000 * x**2 per x in [0,10]
    estrazioni = []
    for i in range(n):
        if y[i] <= 3/1000 * x[i]**2:
            estrazioni.append(x[i])
    return estrazioni

plt.figure(figsize=(10, 5))
plt.hist(parabola(150000), bins=50, density=True, alpha=0.5, label='Hit/Miss', color='orange', ec='darkorange')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Hit/Miss")
plt.legend()
plt.show()