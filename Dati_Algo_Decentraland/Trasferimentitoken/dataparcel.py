import csv
import json
import time
from datetime import datetime
import operator
with open("../Dati/Dati_TrasferToken/parcelnoest.json","r")as file:
   parcel=json.load(file)
maxdata=0
mindata=999999999999
parcel2={}
for i in parcel:
   el={int(i):parcel[i]}
   parcel2.update(el)
sortedDict=sorted(parcel2.items(), key=(operator.itemgetter(0)))
dictp=dict(sortedDict)
for elem in dictp:
   for elem2 in dictp[elem]:
      if int(elem2["data"])> int(maxdata):
         maxdata=elem2["data"]
      if int(elem2["data"])< int(mindata):
         mindata=elem2["data"]
maxdatat=datetime.fromtimestamp(int(maxdata))
mindatat=datetime.fromtimestamp(int(mindata)) 
print("maxdata",maxdatat,"mindata",mindatat,mindata)     