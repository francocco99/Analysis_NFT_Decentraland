import  requests
import json
import os

req="https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x0f5d2fb29fb7d3cfee444a200298f468908cc942&startblock=asd&endblock=asd&apikey=" #apikey da inserire
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
         if not os.path.exists("../Dati/Dati_TrasferToken/risultatimanaest.json"):
            with  open('../Dati/Dati_TrasferToken/risultatimanaest.json','w') as file:
               json.dump(data,file)
         else:
            with  open('../Dati/Dati_TrasferToken/risultatimanaest.json','r+') as file:
               oldl=json.load(file)
               le=len(oldl["result"])
               oldl["result"]=oldl["result"]+temp
               file.seek(0)
               json.dump(oldl,file)
print("FINITO")
