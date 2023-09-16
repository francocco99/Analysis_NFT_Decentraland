
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#GRAFICO VARIAZIONI DI PREZZO PARCEL 1° METODO
with open("../Dati/Dati_Grafi/parcelnoest.json","r")as file:
   parcel=json.load(file)
fig, ax = plt.subplots(figsize=(10, 8))

pricetransf={}
parcel2={}
for i in range(30):
   el={i:[]}
   pricetransf.update(el)

for i in parcel:
   parcel2.update({i:[]})
   lastval=0
   for e2 in parcel[i]:
      diff=e2["price"]-lastval
      parcel2[i].append(diff)
      lastval=e2["price"]

for i in parcel2:
   j=0
   for e2 in parcel2[i]:
      if j<30:
         pricetransf[j].append(round(e2,2))
         j=j+1
price=[]
for i in pricetransf:
   price.append(pricetransf[i])

plt.xlabel("Numero Scambi")
plt.ylabel("Variazione di Prezzo")
vcp=np.array(price)
plt.yscale('symlog')
plt.boxplot(vcp)

plt.savefig("Risultati/boxprezzivar.png")


