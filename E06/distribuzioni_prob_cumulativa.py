import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms

N = 15000
z = np.random.uniform(0, 1, N)
# Ricavo la cumulativa come integrale definito tra 0 e x
cum = z**3 / 1000
# Ricavo l'inversa analiticamente
inv_cum = 10*np.sqrt(z**(1/3))

def inversa_cumulativa(n):
    z = np.random.uniform(0, 1, n)
    return 10*np.sqrt(z**(1/3))

plt.figure(figsize=(10, 5))
plt.hist(inversa_cumulativa(15000), bins=50, density=True, alpha=0.5, label='Inversa Cumulativa', color='blue', ec='darkblue')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Distribuzione di probabilità")
plt.legend()
plt.show()