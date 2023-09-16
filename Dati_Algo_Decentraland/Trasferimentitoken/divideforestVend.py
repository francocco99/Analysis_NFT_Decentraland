import json
from datetime import datetime

with  open('../Dati/Dati_TrasferToken/risultatimanaest.json','r') as file:
   data=json.load(file)
with  open('../Dati/Dati_TrasferToken/risultatiwethest.json','r') as file:
   data2=json.load(file)
with  open('../Dati/Dati_TrasferToken/listest.json','r') as file:
   transf=json.load(file)

with  open('../Dati/Dati_TrasferToken/risultatiesteth.json','r') as file:
   data3=json.load(file)

with open('../Dati/Dati_TrasferToken/hash2.json','r') as file:
   hash=json.load(file)
listdict={}
mana=data["result"]
weth=data2['result']
eth=data3['result']

for elem in mana:
   if elem["hash"] in hash.keys():
      el={"from":elem["from"],"to":elem["to"],"data":elem["timeStamp"],"price":elem["value"],"valuta":elem["tokenSymbol"],"Hash":elem["hash"],"Block":elem["blockNumber"]}
      if hash[elem["hash"]]  not in listdict.keys():   
         new={hash[elem["hash"]]:[el]}
         listdict.update(new)
      else:
         listdict[hash[elem["hash"]]].append(el)

for elem in weth:
   if elem["hash"] in hash.keys():
      el={"from":elem["from"],"to":elem["to"],"data":elem["timeStamp"],"price":elem["value"],"valuta":elem["tokenSymbol"],"Hash":elem["hash"],"Block":elem["blockNumber"]}
      if hash[elem["hash"]]  not in listdict.keys():   
         new={hash[elem["hash"]]:[el]}
         listdict.update(new)
      else:
         listdict[hash[elem["hash"]]].append(el)

for elem in eth:
   if elem["hash"] in hash.keys():
      el={"from":elem["from"],"to":elem["to"],"data":elem["timeStamp"],"price":elem["value"],"valuta":"ETH","Hash":elem["hash"],"Block":elem["blockNumber"]}
      if hash[elem["hash"]]  not in listdict.keys():   
         new={hash[elem["hash"]]:[el]}
         listdict.update(new)
      else:
         listdict[hash[elem["hash"]]].append(el)

         
for elem in transf:
   if elem in listdict.keys():
      for elem2 in transf[elem]:
         for elem3 in listdict[elem]:
            #if (elem2["from"]==elem3["to"]) & (elem2["to"]==elem3["from"]) & (elem2["data"]==elem3["data"]):
            if (elem2["data"]==elem3["data"]) & (elem2["hash"]==elem3["Hash"]):
               elem2["price"]=float(elem2["price"])+float(elem3["price"])
               elem2["tokenName"]=elem3["valuta"]

with open('../Dati/Dati_TrasferToken/estatemanaweth.json','w') as file:
   json.dump(transf,file)
