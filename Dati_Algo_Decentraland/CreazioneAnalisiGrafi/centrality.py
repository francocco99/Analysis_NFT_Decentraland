from cProfile import label
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
degree=nx.degree_centrality(G)
with open("../Dati/Dati_Grafi/centrality.json",'w') as file:
   json.dump(degree,file)

print("name,centrality")
for elem in degree:
   print(str(elem)+','+str(degree[elem]))
