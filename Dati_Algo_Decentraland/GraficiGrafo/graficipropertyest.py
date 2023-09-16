
import json
import matplotlib.pyplot as plt

#GRAFICO PROPRIETà ACCOUNT ESTATE
with open("../Dati/Dati_Grafi/property.json","r") as file:
   bal=json.load(file)
acq=[]
ott=[]
for el in bal:
   acq.append(bal[el]['Estate_Acquistati'])
   ott.append(bal[el]['Estate_Ottenuti'])
fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure containing a single axes.
ax.plot(acq,ott,'ko')
plt.xscale('symlog')
plt.yscale('symlog')
plt.plot([0, 1000000], [0, 1000000], 'k')
plt.title("Grafico  Estate")
plt.xlabel("Estate Acquistati")
plt.ylabel("Estate Ottenuti")
ax.autoscale(enable=True,axis='both',tight='None')
plt.tight_layout()
plt.savefig("Risultati/propertyest.png")
