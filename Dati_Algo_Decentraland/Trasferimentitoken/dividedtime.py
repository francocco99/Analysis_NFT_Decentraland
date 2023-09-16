import json

with open("../Dati/Dati_TrasferToken/parcelmanaweth.json","r")as file:
   parcel=json.load(file)
time={}
div=1000000000000000000
for el in parcel:
   for j in parcel[el]:
      ok=False
      if j['data'] not in time.keys():
         riga={j['data']:[]}
         time.update(riga)
         elem={'price':j['price'],'Tname':j['tokenName'],'from':j['from'],'to':j['to'],'number':1,'hash':j['hash']}
         time[j['data']].append(elem)
      else:
         for i in time[j['data']]:
            if (i['from']==j['from']) & (i['to']==j['to']) & (i['hash']==j['hash']):
               ok=True
               i['number']=i['number']+1
               if j['price']!=0:
                  i['price']=j['price']
                  i['Tname']=j['tokenName']
         if ok==False:
            elem={'price':j['price'],'Tname':j['tokenName'],'from':j['from'],'to':j['to'],'number':1,'hash':j['hash']}
            time[j['data']].append(elem)


         
with open("../Dati/Dati_TrasferToken/timepar.json","w")as file:
   parcel=json.dump(time,file)
"""
for e in time:
   for i in time[e]:
      realprice=float(i["price"])/div
      if realprice!=0:
         if i['number']>1:
            print(i,'-------------------------->',realprice)
"""