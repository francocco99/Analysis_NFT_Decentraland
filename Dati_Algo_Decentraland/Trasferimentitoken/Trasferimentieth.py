import  requests
import json
import os

req="https://api.etherscan.io/api?module=account&action=txlistinternal&startblock=asd&endblock=asd&apikey=7PEM6GJ6R5BSK49UX4Y2A86QGY5MNQ1T2G"
plhold="asd"


status=1
with  open('../Dati/Dati_TrasferToken/blockest2.json','r+') as file:
   block=json.load(file)

for elem in block:
   if elem > 14028889:
      query=req.replace(plhold,str(elem))
      response=requests.get(query)
      if response.status_code==200:
         data=json.loads(response.text)
         
         temp=data["result"]
         status=data["status"]
         if int(status)==1:
            if not os.path.exists("../Dati/Dati_TrasferToken/risultatiesteth.json"):
               with  open("../Dati/Dati_TrasferToken/risultatiesteth.json",'w') as file:
                  json.dump(data,file)
            else:
               with  open("../Dati/Dati_TrasferToken/risultatiesteth.json",'r+') as file:
                  oldl=json.load(file)
                  le=len(oldl["result"])
                  oldl["result"]=oldl["result"]+temp
                  file.seek(0)
                  json.dump(oldl,file)
print("FINITO ETH")
