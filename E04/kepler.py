import pandas as pd
import matplotlib.pyplot as plt

url = "kplr010666592-2011240104155_slc.csv"
df = pd.read_csv(url)

print("Colonne del DataFrame:")
print(df.columns)

plt.figure(figsize=(10, 6))
# plt.plot(df["TIME"],df["PDCSAP_FLUX"],color="blue",linewidth=0.5)
# plt.plot(df["TIME"],df["PDCSAP_FLUX"],"o",markersize=2,color="black")
plt.errorbar(df["TIME"],df["PDCSAP_FLUX"],yerr=df["PDCSAP_FLUX_ERR"],fmt=".",color="purple",ecolor="lightgray",elinewidth=0.5)
plt.xlabel("Time (BJD - 2454833)")
plt.ylabel("Flux (e-/s)")
plt.title("Flusso di luce in funzione del tempo")
plt.savefig("flusso_luce.png", dpi=300)
plt.savefig("flusso_luce.pdf")
plt.show()

