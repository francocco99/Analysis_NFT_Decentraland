import csv
import json
import time
from datetime import date

div=1000000000000000000
changem={}
changeE={}
with open("../Dati/Dati_TrasferToken/parcelmanaweth.json","r")as file:
   parcel=json.load(file)
with open("../Dati/Dati_TrasferToken/MANA-USD.csv","r",encoding='utf-8-sig')as file:
   dollar=csv.reader(file)
   for i in dollar:
      #time_t=time.mktime(datetime.datetime.strptime(i[0], "%Y-%m-%d").timetuple())
      changem.update({i[0]:i[4]})
with open("../Dati/Dati_TrasferToken/ETH-USD.csv","r",encoding='utf-8-sig')as file:
   dollar=csv.reader(file)
   for i in dollar:
      #time_t=time.mktime(datetime.datetime.strptime(i[0], "%Y-%m-%d").timetuple())
      changeE.update({i[0]:i[4]})


for elem in parcel.values():
   for elem2 in elem:
      date=date.fromtimestamp(int(elem2["data"]))

      if elem2['price']!=0:
         if elem2['tokenName']=='MANA':
            cvalue=changem[str(date)]
            price=float(cvalue)*(elem2['price']/div)
            elem2['price']=price
            elem2['tokenName']='dollar'
         else:
            cvalue=changeE[str(date)]
            price=float(cvalue)*(elem2['price']/div)
            elem2['price']=price
            elem2['tokenName']='dollar'
      
with open("../Dati/Dati_TrasferToken/parceldollar.json","w")as file:
   json.dump(parcel,file) 
