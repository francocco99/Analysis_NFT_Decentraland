import json
with open('../Dati/Dati_TrasferToken/parcelmanaweth.json') as file:
   parcel=json.load(file)
listst={}
total=0
vend=0
trasf=0
for elem in parcel:
   for elem2 in parcel[elem]:
      total=total+1
      if elem2["price"]!=0:
         vend=vend+1
      else:
         trasf=trasf+1
print('total:',total,'vendite:',vend,'trasferimenti:',trasf)