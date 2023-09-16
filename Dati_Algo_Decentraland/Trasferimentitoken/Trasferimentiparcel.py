import  requests
import json

req4="https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d&apikey=" #apikey da inserire
req7="https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d&startblock=asd&endblock=99999999&apikey=" #apikey da inserire

ok=True
plhold="asd"
response=requests.get(req4)
data1=json.loads(response.text)
with  open('../Dati/Dati_TrasferToken/trasferimenti.json','w') as outfile:
   json.dump(data1,outfile)
dataelab=data1["result"]
le=len(dataelab)
last=dataelab[le-1]["blockNumber"]

wh=True
status=data1["status"]

while wh:
   query=req7.replace(plhold,last)
   response=requests.get(query)
   if response.status_code==200:
      data=json.loads(response.text)
      temp=data["result"]
      status=data["status"]
      if int(status)==1:
         with  open('../Dati/Dati_TrasferTokenultati/trasferimenti.json','r+') as file:
            oldl=json.load(file)
            le=len(oldl["result"])
            i=le-1
            while ok:
               if oldl["result"][i]["blockNumber"]==last:
                  del  oldl["result"][i]
                  i=i-1
               else:
                  ok=False
            ok=True
            oldl["result"]=oldl["result"]+temp
            file.seek(0)
            json.dump(oldl,file)
         last=temp[len(temp)-1]['blockNumber']
         if int(last)==14409428:
            wh=False
      else:
         wh=False
print("FINITO")
