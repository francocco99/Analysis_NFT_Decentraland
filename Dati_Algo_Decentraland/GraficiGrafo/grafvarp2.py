
import json

import matplotlib.pyplot as plt
import numpy as np

#GRAFICO VARIAZIONI DI PREZZO PARCEL 2° METODO
with open("../Dati/Dati_Grafi/parcelnoest.json","r")as file:
   parcel=json.load(file)
fig, ax = plt.subplots(figsize=(10, 8))

pricetransf={}
parcel2={}
parcel3={}
for i in range(30):
   el={i:[]}
   pricetransf.update(el)

for i in parcel:
   parcel2.update({i:[]})
   lastp=0
   for e2 in parcel[i]:
      if (e2['price']==0):
         parcel2[i].append(lastp)
      else:
         parcel2[i].append(e2["price"])
         lastp=e2["price"]
for i in parcel2:
   parcel3.update({i:[]})
   lastval=0
   for e2 in parcel2[i]:
      diff=e2-lastval
      parcel3[i].append(diff)
      lastval=e2



for i in parcel3:
   j=0
   for e2 in parcel3[i]:
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
#plt.show()
plt.savefig("Risultati/boxprezzivarno0.png")
#print(type(df))
