import json
from datetime import datetime

with  open('../Dati/Dati_TrasferToken/risultatimana.json','r') as file:
   data=json.load(file)
with  open('../Dati/Dati_TrasferToken/risultatiwethm.json','r') as file:
   weth=json.load(file)
with  open('../Dati/Dati_TrasferToken/listparcel.json','r') as file:
   transf=json.load(file)
with  open('../Dati/Dati_TrasferToken/risultatieth.json','r') as file:
   data2=json.load(file)
with open('../Dati/Dati_TrasferToken/hash.json','r') as file:
   hash=json.load(file)
listdict={}
mana=data["result"]
eth=data2['result']
#weth=data["result"]
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

with open('../Dati/Dati_TrasferToken/parcelmanaweth.json','w') as file:
   json.dump(transf,file)
