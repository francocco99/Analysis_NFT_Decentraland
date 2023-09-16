import  requests
import json
import os

req="https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&startblock=asd&endblock=asd&apikey=" # apikey da inserire
plhold="asd"


status=1
with  open('../Dati/Dati_TrasferToken/blockest.json','r+') as file:
   block=json.load(file)

for elem in block:
   query=req.replace(plhold,str(elem))
   response=requests.get(query)
   if response.status_code==200:
      data=json.loads(response.text)
      temp=data["result"]
      status=data["status"]
      if int(status)==1:
         if not os.path.exists("../Dati/Dati_TrasferToken/risultatiwethest.json"):
            with  open("../Dati/Dati_TrasferToken/risultatiwethest.json",'w') as file:
               json.dump(data,file)
         else:
            with  open("../Dati/Dati_TrasferToken/risultatiwethest.json",'r+') as file:
               oldl=json.load(file)
               le=len(oldl["result"])
               oldl["result"]=oldl["result"]+temp
               file.seek(0)
               json.dump(oldl,file)
print("FINITO WETH")
