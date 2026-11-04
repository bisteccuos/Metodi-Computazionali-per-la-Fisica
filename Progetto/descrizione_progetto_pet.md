# Progetto: Simulazione di un Sistema PET (Tomografia ad Emissione di Positroni)

La **Tomografia ad Emissione di Positroni** (*Positron Emission Tomography* - **PET**) è una tecnica diagnostica di medicina nucleare particolarmente utile per lo studio della fisiologia del paziente, ad esempio nel tracciamento e nell'analisi di malattie neoplastiche ([Wikipedia - PET](https://it.wikipedia.org/wiki/Tomografia_a_emissione_di_positroni)).

---

## Principio fisico

La PET si basa sull'utilizzo di sostanze radioattive (traccianti) iniettate nel paziente che decadono tramite **decadimento $\beta^+$**:

$$p \to n + e^+ + \nu_e$$

Il processo prevede l'emissione di un **positrone** ($e^+$) che, dopo aver percorso una breve distanza all'interno del tessuto corporeo, **annichila** interagendo con un elettrone ($e^-$) del mezzo:

$$e^+ + e^- \to \gamma + \gamma$$

L'annichilazione genera due fotoni $\gamma$ ciascuno con energia pari a $511\text{ keV}$, emessi in direzioni quasi perfettamente diametralmente opposte (a $180^\circ$).

---

## Rivelazione dei fotoni

I fotoni vengono rivelati da una serie di sensori disposti lungo una **corona circolare** attorno al paziente. Quando due fotoni vengono registrati da elementi diametralmente opposti entro una finestra temporale ristretta (coincidenza temporale), viene identificata una linea di risposta (*Line of Response* - LOR).

Nei sistemi avanzati a **Tempo di Volo** (*Time-of-Flight* - **TOF-PET**), caratterizzati da una spiccata risoluzione temporale, la minima differenza nel tempo di arrivo dei due fotoni ($\Delta t$) consente di risalire direttamente alla posizione del punto di emissione lungo la LOR.

---

## Dettagli del progetto software

1. **Sviluppo del pacchetto software:**
   - Definire un'architettura software a oggetti per modellare un sistema PET.
   - Rendere il sistema ampiamente configurabile nei parametri costruttivi e operativi (es. dimensioni della corona, numero di pixel/detector, risoluzione spaziale, risoluzione temporale, efficienza di rivelazione).

2. **Simulazione e analisi:**
   - Utilizzare il pacchetto sviluppato per simulare diverse configurazioni del sistema.
   - Confrontare la qualità delle immagini diagnostiche ottenute (o del profilo di ricostruzione) al variare dei diversi parametri del rivelatore.

---

## Suggerimenti tecnici
- Risoluzioni temporali adeguate per la simulazione del tempo di volo (TOF) sono dell'ordine dei **nanosecondi** ($\text{ns}$) o di **frazioni di nanosecondo** (es. $200\text{ ps} - 500\text{ ps}$).