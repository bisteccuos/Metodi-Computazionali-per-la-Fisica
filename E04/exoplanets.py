import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

data = os.path.dirname(os.path.abspath(__file__))
url = os.path.join(data,"ExoplanetsPars_2025.csv")
df = pd.read_csv(url,comment="#")

print("Colonne del DataFrame:")
print(df.columns)

print("Estratto del DataFrame:")
print(df.head())

# R_max corrisponde al semiasse maggiore dell'orbita e m* alla massa stellare
plt.figure(figsize=(10, 6))

val_y = (df["pl_orbsmax"]**2 / df["st_mass"])

# plt.scatter(df["pl_orbper"], df["pl_bmasse"],alpha=0.5,s=10,color="blue")
plt.scatter(df["pl_orbper"],val_y,alpha=0.5,s=10,color="blue")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo orbitale (giorni)")
plt.ylabel("Massa del pianeta (masse terrestri)")
# plt.title("Massa del pianeta in funzione del periodo orbitale (log-log)")
plt.title("Rapporto $R_{max}^2/M_*$ in funzione del periodo orbitale (log-log)")
plt.grid(True,which="both",ls="--",alpha=0.5)
plt.show()