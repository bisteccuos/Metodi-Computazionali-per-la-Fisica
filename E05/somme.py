import numpy as np

def somma_n(n):
	somman = 0
	for i in range(n):
		somman = somman+i
	return somman

def somma_rad(n):
	sommarad = 0.0
	for i in range(n):
		sommarad = sommarad+np.sqrt(i)
	return sommarad

def som_prod(n):
	som = 0
	prod = 1
	for i in range(n):
		som = som+i
		prod = prod*i
	return som,prod

def serie(n,alpha=1):
	sum = 0.0
	for i in range(n):
		sum = sum+i**alpha
	return sum
