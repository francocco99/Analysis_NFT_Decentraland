import json
import matplotlib.pyplot as plt
#GRAFICO DEGREE PARCEL VENDITE
with open("../Dati/Dati_Grafi/degreesell.json","r") as file:
   deg=json.load(file)
outdeg=[]
indeg=[]
for el in deg:
   indeg.append(deg[el]['Indegree'])
   outdeg.append(deg[el]['Outdegree'])
fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure containing a single axes.
ax.plot(outdeg,indeg,'ko')
plt.xscale('symlog')
plt.yscale('symlog')
plt.plot([0, 1000000], [0, 1000000], 'k')
plt.title("Grafico indegree outdegree")
plt.xlabel("Out Degree")
plt.ylabel("In Degree")
ax.autoscale(enable=True,axis='both',tight='None')
plt.tight_layout()

plt.savefig("Risultati/degreeparvend.png")
#plt.show()
