import numpy as np

valore1 = input('Inserire un valore intero: ')
valore2 = input('Inserirne un altro: ')

# Conversione da stringa ad intero
val1 = int(valore1)
val2 = int(valore2)

# Conversione in binario
val1_bin = bin(val1)
val2_bin = bin(val2)
print("I valori inseriti in rappresentazione binaria sono:\n",val1_bin,"\n",val2_bin,"\n")

# Conversione in esadecimale
val1_hex = hex(val1)
val2_hex = hex(val2)
print("I valori inseriti in rappresentazione esadecimale sono:\n",val1_hex,"\n",val2_hex,"\n")

''' Gli operatori bitwise lavorano solo con gli interi e non con le stringhe che bin() ed hex()
restituiscono. Per questo bisogna passare all'AND e all'OR i valori interi e poi rappresentare in
bin() ed hex() il risultato del bitwise. '''

and_out = val1&val2
or_out = val1|val2

# Operazione AND/OR in binario
print("AND/OR in rappresentazione binaria:\n")
print(f"val1 & val2 : {and_out:06b}")
print(f"(val1|val2) : {or_out:06b}\n")

# Operazione AND/OR in esadecimale
print("AND/OR in rappresentazione esadecimale:\n")
print(f"val1 & val2 : {and_out:06x}")
print(f"val1 | val2 : {or_out:06x}")
