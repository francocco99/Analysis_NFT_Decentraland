
import json
import matplotlib.pyplot as plt

#GRAFICO PROPRIETà ACCOUNT PARCEL
with open("../Dati/Dati_Grafi/property.json","r") as file:
   bal=json.load(file)
acq=[]
ott=[]
for el in bal:
   acq.append(bal[el]['Parcel_Acquistati'])
   ott.append(bal[el]['Parcel_Ottenuti'])
fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure containing a single axes.
plt.tight_layout()
ax.plot(acq,ott,'ko')
plt.xscale('symlog')
plt.yscale('symlog')
plt.plot([0, 1000000], [0, 1000000], 'k')
plt.title("Grafico  Parcel")
plt.xlabel("Parcel Acquistati")
plt.ylabel("Parcel Ottenuti")
ax.autoscale(enable=True,axis='both',tight='None')
plt.tight_layout()
plt.savefig("Risultati/propertyparc.png")
