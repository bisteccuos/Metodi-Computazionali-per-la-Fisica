import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = os.path.dirname(os.path.abspath(__file__))
url = os.path.join(data, "ExoplanetsPars_2025.csv")
df = pd.read_csv(url, comment="#")

print("Colonne del DataFrame:")
print(df.columns)

print("Estratto del DataFrame:")
print(df.head())

# Massa del pianeta in funzione del periodo orbitale
plt.figure(figsize=(10, 6))
plt.scatter(df["pl_orbper"], df["pl_bmasse"], alpha=0.5, s=10, color="blue")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo orbitale (giorni)")
plt.ylabel("Massa del pianeta (masse terrestri)")
plt.title("Massa del pianeta in funzione del periodo orbitale (log-log)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# R_max corrisponde al semiasse maggiore dell'orbita e m* alla massa stellare
plt.figure(figsize=(10, 6))

val_y = df["pl_orbsmax"] ** 2 / df["st_mass"]

plt.scatter(df["pl_orbper"], val_y, alpha=0.5, s=10, color="blue")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo orbitale (giorni)")
plt.ylabel("Rapporto $R_{max}^2/M_*$")
plt.title("Rapporto $R_{max}^2/M_*$ in funzione del periodo orbitale (log-log)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# Grafico che distingue gli esopianeti per metodo di scoperta
df_transit = df.loc[df["discoverymethod"] == "Transit"]  # così prendo solo quelli scoperti con transit
df_rv = df.loc[df["discoverymethod"] == "Radial Velocity"]  # così prendo solo quelli scoperti con radial velocity
# si usa loc per la selezione dei valori nel DataFrame, in questo caso si selezionano le righe in cui la colonna discoverymethod è uguale a "Transit" o "Radial Velocity"
plt.figure(figsize=(10, 6))
plt.scatter(df_transit["pl_orbper"],df_transit["pl_bmasse"],alpha=0.5,s=12,color="blue",label="Transit",)
plt.scatter(df_rv["pl_orbper"],df_rv["pl_bmasse"],alpha=0.5,s=12,color="red",label="Radial Velocity")
# alpha è utile per la trasparenza dei punti, così da vedere meglio le zone più dense di punti

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo orbitale (giorni)")
plt.ylabel("Massa del pianeta (masse terrestri)")
plt.title("Massa del pianeta in funzione del metodo di scoperta (log-log)")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# Istogramma della massa dei pianeti distinguendo esopianeti per metodo di scoperta
plt.figure(figsize=(10, 6))
# devo trovare un numero di bin che sia uguale sia per la distribuzione dei pianeti scoperti con il metodo del transito sia per quelli scoperti con il metodo della velocità radiale
# per trovare il numero di bin considero l'intervallo tra il valore minimo e quello massimo della massa dei pianeti scoperti con i due metodi
val_min = min(df_transit.min(), df_rv.min())
val_max = max(df_transit.max(), df_rv.max())
# i bin li faccio in scala logaritmica
bins = np.logspace(np.log10(val_min), np.log10(val_max), 50)  # così mi genera 50 intervalli tra max e min
plt.hist(df_transit["pl_bmasse"],bins=bins,alpha=0.5,color="blue",label="Transit",edgecolor="black",linewidth=0.5)
plt.hist(df_rv["pl_bmasse"],bins=bins,alpha=0.5,color="red",label="Radial Velocity",edgecolor="black",linewidth=0.5)

plt.xscale("log")
plt.xlabel("Massa del pianeta (masse terrestri)")
plt.ylabel("Frequenza")
plt.title("Istogramma della massa dei pianeti in funzione del metodo di scoperta (log-log)")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# istogramma per il logaritmo in base 10 della massa dei pianeti
""" cioè faccio grafico della distribuzione delle masse ma applico il logaritmo
perchè senza vedrei la maggior parte dei valori prossimi allo zero
in quanto le masse sono tendenzialmente piccole"""
log_mass_transit = np.log10(df_transit["pl_bmasse"])
log_mass_rv = np.log10(df_rv["pl_bmasse"])

min_log = min(log_mass_transit.min(), log_mass_rv.min())
max_log = max(log_mass_transit.max(), log_mass_rv.max())
bins_log = np.linspace(min_log, max_log, 50)

plt.figure(figsize=(10, 6))
plt.hist(log_mass_transit,bins=bins_log,alpha=0.5,color="blue",label="Transit",edgecolor="black",linewidth=0.5)
plt.hist(log_mass_rv,bins=bins_log,alpha=0.5,color="red",label="Radial Velocity",edgecolor="black",linewidth=0.5)

plt.xlabel("Massa del pianeta (log10(masse terrestri))")
plt.ylabel("Frequenza")
plt.title("Istogramma del logaritmo in base 10 della massa dei pianeti in funzione del metodo di scoperta")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()