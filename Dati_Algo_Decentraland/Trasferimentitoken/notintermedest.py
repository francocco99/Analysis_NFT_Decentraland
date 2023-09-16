import requests
import json
import os
from datetime import datetime
with  open('../Dati/Dati_TrasferToken/estatedollar.json','r') as outfile:
   sales=json.load(outfile)


for e in sales:
   for e2 in sales[e]:
      
      if e2['to']=="0xe479dfd9664c693b2e2992300930b00bfde08233":
         rto=e2['from']
         
      if e2['from']=="0xe479dfd9664c693b2e2992300930b00bfde08233":
         e2['from']=rto
for e in sales:
   for e2 in sales[e]:
      if e2['to']=="0xe479dfd9664c693b2e2992300930b00bfde08233":
         sales[e].remove(e2)
         
      
with  open('../Dati/Dati_TrasferToken/estatedollarnoint.json','w') as outfile:
   json.dump(sales,outfile)