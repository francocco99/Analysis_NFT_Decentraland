import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import json
import tkinter 
from networkx.readwrite import json_graph
import  scipy as scp

with open("../Dati/Dati_Grafi/graphfilereal.json","r") as file:
   data=json.load(file)
G = json_graph.node_link_graph(data)
price = nx.get_edge_attributes(G,"price")
weight={}
for n in price:
   if price[n]==0:
      if n[0] in weight:
         weight[n[0]]["free"]=weight[n[0]]["free"]+1
      else:
         weight.update({n[0]:{"free":1,"vend":0}})
      if n[1] in weight:
         weight[n[1]]["free"]=weight[n[1]]["free"]+1
      else:
         weight.update({n[1]:{"free":1,"vend":0}})
   else:
      if n[0] in weight:
         weight[n[0]]["vend"]=weight[n[0]]["vend"]+1
      else:
         weight.update({n[0]:{"free":0,"vend":1}})
      if n[1] in weight:
         weight[n[1]]["vend"]=weight[n[1]]["vend"]+1
      else:
         weight.update({n[1]:{"free":0,"vend":1}})
"""
for i in weight:
   print(i,"transf",weight[i]["free"],"vend",weight[i]["vend"],"total",G.degree(i))

print("name,trasferimenti,vendite")
for i in weight:
   print(i+","+str(weight[i]["free"])+","+str(weight[i]["vend"]))
"""
with open("../Dati/Dati_Grafi/weightedge.json","w") as file:
   json.dump(weight,file)