import csv
import json
import time
from datetime import datetime
import operator
with open("../Dati/Dati_TrasferToken/parceldollardef.json","r")as file:
   parcel=json.load(file)
parcel2={}
for i in parcel:
   el={int(i):parcel[i]}
   parcel2.update(el)
sortedDict=sorted(parcel2.items(), key=(operator.itemgetter(0)))
dictp=dict(sortedDict)

for elem in dictp:
   for elem2 in reversed(dictp[elem]):
      if (elem2["from"]=="0x959e104e1a4db6317fa58f8295f586e1a978c297") | (elem2["to"]=="0x959e104e1a4db6317fa58f8295f586e1a978c297"):
         dictp[elem].remove(elem2)
with open("../Dati/Dati_TrasferToken/parcelnoest.json","w")as file:
   json.dump(dictp,file)