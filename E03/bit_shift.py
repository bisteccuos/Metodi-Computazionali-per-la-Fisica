import numpy as np

valore = input("Inserire un valore intero: ")
bit = input("Di quanti bit effettuare lo shift: ")

val = int(valore)
n_bit = int(bit)
val_bin = bin(val)
val_hex = hex(val)

print("\nIl valore in rappresentazione binaria è: ",val_bin)
print("Il valore in rappresentazione esadecimale è: ",val_hex,"\n")

# Bit shift aggiunta/sottrazione binaria
val_agg1 = (val << n_bit)
val_sott1 = (val >> n_bit)

val_agg_bin = bin(val_agg1)
val_sott_bin = bin(val_sott1)

print("--- Bit shift in rappresentazione binaria ---\n")
print("Aggiunta <<: ",val_agg_bin)
print("Sottrazione >>: ",val_sott_bin,"\n")

# Bit shift aggiunta/sottrazione esadecimale
val_agg2 = (val << n_bit)
val_sott2 = (val >> n_bit)

val_agg_hex = hex(val_agg2)
val_sott_hex = hex(val_sott2)

print("--- Bit shift in rappresentazione esadecimale ---")
print("Aggiunta <<: ",val_agg_hex)
print("Sottrazione >>: ",val_sott_hex,"\n")
