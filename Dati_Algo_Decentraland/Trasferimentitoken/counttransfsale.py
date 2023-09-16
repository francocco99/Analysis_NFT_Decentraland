import json


with open('../Dati/Dati_TrasferToken/parcelmanaweth.json') as file:
   parcel=json.load(file)
listst={}
for elem in parcel:
   v=0
   t=0
   tot=0
   for elem2 in parcel[elem]:
      tot=tot+1
      if elem2["price"]!=0:
         v=v+1
      else:
         t+=1
   new={"vendite":v,"trasfer":t,"totale":tot}
   listst.update({elem:new})
with open('../Dati/Dati_TrasferToken/countparcel.json','w') as file:
   json.dump(listst,file)
total=0
numbert=0
numberv=0
equal=0
for elem in listst:
   total=total+1
   if listst[elem]["vendite"]> listst[elem]["trasfer"]:
      numberv=numberv+1
   elif listst[elem]["trasfer"]> listst[elem]["vendite"]:
      numbert=numbert+1
   else: 
      equal=equal+1
   print(elem+"\n","VENDITE",listst[elem]["vendite"],"TRASFERIMENTI",listst[elem]["trasfer"],"TOTALE",listst[elem]["totale"])
print("numero totale di parcel",total,"\nnumero di vendite >",numberv,"\nnumero di trasferimenti >",numbert,"\nnumero di equal",equal)