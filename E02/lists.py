import numpy as np

# Lista con i nomi dei giorni della settimana per tutto il mese di ottobre 2026
settimana = ['Giovedì','Venerdì','Sabato','Domenica','Lunedì','Martedì','Mercoledì']
# Dato che ottobre inizia di giovedì, ripeto la settimana 4 volte e aggiungo i giorni extra
extra = ['Giovedì','Venerdì','Sabato']
giorni = settimana*4 + extra
# Lista dei numeri dei giorni
numeri = []
for i in range(1,32):
	numeri.append(i)
# Dizionario da riempire: per ogni numero da 1 a 31 incluso
ottobre = dict(zip(numeri,giorni))
for i in ottobre:
	print(f"{i: <1} - {ottobre[i]}")
