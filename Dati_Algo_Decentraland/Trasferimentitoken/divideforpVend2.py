import requests
import json
import os
from datetime import datetime
with  open('../Dati/Dati_TrasferToken/parcelmanaweth.json','r') as outfile:
   sales=json.load(outfile)
with  open('../Dati/Dati_TrasferToken/timepar.json','r') as outfile:
   time=json.load(outfile)
for e in sales:
   for e2 in sales[e]:
         #if e2['price']==0:
      for j in time[e2['data']]:
         if (j['number']>1) & (j['price']>0):
            if (j['from']==e2['from']) & (j['to']==e2['to']):
               realprice=round(j['price']/j['number'],2)
               e2['price']=realprice
               #print(j['Tname'])
               e2['tokenName']=j['Tname']
               e2['totale']=float(j['price'])

with  open('../Dati/Dati_TrasferToken/parcelmanaweth2.json','w') as outfile:
   json.dump(sales,outfile)