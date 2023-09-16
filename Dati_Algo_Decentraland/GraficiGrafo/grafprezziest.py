
import json

import matplotlib.pyplot as plt
import numpy as np

#GRAFICO DEI PREZZI ESTATE 1° METODO
with open("../Dati/Dati_Grafi/estatedollarnoint.json","r")as file:
   parcel=json.load(file)
fig, ax = plt.subplots(figsize=(10, 8))

pricetransf={}
for i in range(12):
   el={i:[]}
   pricetransf.update(el)


for i in parcel:
   j=0
   for e2 in parcel[i]:
      pricetransf[j].append(round(e2['price'],2))
      j=j+1
price=[]
for i in pricetransf:
   price.append(pricetransf[i])

plt.xlabel("Numero Scambi")
plt.ylabel("Prezzo di vendita")
vcp=np.array(price)
plt.yscale('symlog')
plt.boxplot(vcp)

plt.savefig("Risultati/boxprezziest.png")


