import json
from datetime import datetime

with  open('../Dati/Dati_TrasferToken/trasferimentiest.json','r+') as file:
  transf=json.load(file)
data=transf["result"]
parceltransf={}
for elem in data:
   el={"from":elem["from"],"to":elem["to"],"data":elem["timeStamp"],"hash":elem["hash"],"price":0,"tokenName":"Null","Block":elem['blockNumber']}
   if elem["tokenID"]  not in parceltransf.keys():   
      new={elem["tokenID"]:[el]}
      parceltransf.update(new)
   else:
      parceltransf[elem["tokenID"]].append(el)
"""
n=0
for elem in parceltransf:
   for elem2 in parceltransf[elem]:
      n=n+1
print(n)
"""
with open('../Dati/Dati_TrasferToken/listest.json','w') as file:
   json.dump(parceltransf,file)
