import json
import matplotlib.pyplot as plt

#GRAFICO  DIFFERENZA VENDITE TRASFERIMENTI ACCOUNT PARCEL
with open('../Dati/Dati_Grafi/weightedge.json','r') as file:
   listst=json.load(file)
transf=[]
sale=[]
for el in listst:
   transf.append(listst[el]['free'])
   sale.append(listst[el]['vend'])
fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure containing a single axes.
ax.plot(transf,sale,'ko')
plt.title("Grafico delle vendite")
plt.xlabel("trasferimenti")
plt.ylabel("vendite")
plt.xscale('symlog')
plt.yscale('symlog')
plt.plot([0, 1000000], [0, 1000000], 'k')
ax.autoscale(enable=True,axis='both',tight='None')
plt.savefig("Risultati/vend.png")
