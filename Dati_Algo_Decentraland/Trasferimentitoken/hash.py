import json
from datetime import datetime

with  open('../Dati/Dati_TrasferToken/trasferimentiest.json','r+') as file:
   mana=json.load(file)
data=mana['result']
hash={}
for i in data:
   hash.update({i["hash"]:i["tokenID"]})
print(len(hash))
with open('../Dati/Dati_TrasferToken/hash2.json','w')as file:
   json.dump(hash,file)
