
import networkx as nx
import matplotlib.pyplot as plt
import json
from networkx.readwrite import json_graph
import  scipy as scp
import netwulf as nw


div=1000000000000000000
with open("../Dati/Dati_TrasferToken/estatemanaweth.json",'r') as file:
   data=json.load(file)
n=0
l2=[]
attr=[]
for elem in data:
   for elem2 in data[elem]:
      if elem2["price"]!=0:
         n=n+1
         riga=[]
         riga.append(elem2["from"])
         riga.append(elem2["to"])
         realprice=elem2["price"]/div
         riga.append({"tokenId":elem,"price":float(realprice),"tokenName":elem2["tokenName"],"data":elem2["data"]})
         l2.append(tuple(riga))
      
    

G=nx.MultiDiGraph(l2)
data1=json_graph.node_link_data(G)

print(G.number_of_edges())
with open("../Dati/Dati_Grafi/graphfileestsell.json","w") as file:
   json.dump(data1,file)
nx.write_graphml(G,"graphonlysellest.graphml")