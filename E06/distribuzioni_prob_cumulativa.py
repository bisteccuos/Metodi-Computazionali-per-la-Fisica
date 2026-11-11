import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms

N = 15000

def inversa_cumulativa(n):
    z = np.random.uniform(0, 1, n)
    return 10*(z**(1/3))

x_teorica = np.linspace(0,10,100)
y_teorica = 3/1000 * x_teorica**2

plt.figure(figsize=(10, 5))
plt.hist(inversa_cumulativa(15000), bins=50, density=True, alpha=0.5, label='Inversa Cumulativa', color='blue', ec='darkblue')

plt.plot(x_teorica,y_teorica,'r-',linewidth=2,color='yellow')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Distribuzione di probabilità")
plt.legend()
plt.show()