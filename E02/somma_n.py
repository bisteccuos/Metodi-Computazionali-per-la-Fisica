import numpy as np

n = input("Immettere un numero intero n: ")
numero = int(n)
somma = 0
for i in range(1,numero+1):
	somma = somma + i
print("La somma dei primi n numeri naturali è: ",somma)
