import requests
import json
with open('../Dati/Dati_TrasferToken/trasferimentiest.json','r')as file:
   transf=json.load(file)
data=transf['result']
block=[]
for i in data:
   block.append(int(i['blockNumber']))
new=set(block)
newblock = list(new)
newblock.sort()
with open('../Dati/Dati_TrasferToken/blockest.json','w')as file:
   json.dump(newblock,file)
n=0
for i in newblock:
   n=n+1
   print(i,n)