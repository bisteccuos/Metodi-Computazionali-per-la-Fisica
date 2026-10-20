import numpy as np
import datetime
from datetime import datetime,timedelta

# Input data di nascita
y = input("Qual è il tuo anno di nascita? ")
m = input("Di che mese? ")
d = input("E di che giorno? ")

anno = int(y)
mese = int(m)
giorno = int(d)

data_nascita = datetime(anno,mese,giorno)

# Data e orario attuale
ora = datetime.now()
print(f"\nOra sono le {ora.hour}:{ora.minute}:{ora.second} del {ora.day}/{ora.month}/{ora.year}\n")

# Calcolo dell'età
differenza = ora - data_nascita
giorni_totali = differenza.days
secondi_totali = int(differenza.total_seconds())
minuti_totali = secondi_totali // 60
secondi_restanti = secondi_totali - (minuti_totali//60)
eta_anni = giorni_totali // 365 # Così ottengo l'intero più vicino approssimato per difetto

print(f"Hai esattamente:\n{eta_anni} anni;\n{giorni_totali} giorni,\n{differenza} ore;\n{minuti_totali} minuti;\n{secondi_restanti} secondi")
