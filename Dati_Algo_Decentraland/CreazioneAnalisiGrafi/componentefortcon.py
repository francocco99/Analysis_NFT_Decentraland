
import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

with open("../Dati/Dati_Grafi/graphfilereal.json","r") as file:
   graph=json.load(file)
G = json_graph.node_link_graph(graph)
print(G)
numb=nx.number_strongly_connected_components(G)
result1=sorted(nx.strongly_connected_components(G),key=len)
print('numero delle componenti connesse: ',numb)
ultimo=result1[len(result1)-1]
for i in result1:
   print(i,'---------------->',len(i))
