from cProfile import label
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import json
import tkinter 
from networkx.readwrite import json_graph
import  scipy as scp

with open("../Dati/Dati_Grafi/graphfileest.json","r") as file:
   data=json.load(file)
G = json_graph.node_link_graph(data)
degree={}
cent=nx.degree_centrality(G)
for e in G.nodes:
   dg={"degree":G.degree(e),"Indegree":G.in_degree(e),"Outdegree":G.out_degree(e)}
   el={e:dg}
   degree.update(el)
with open("../Dati/Dati_Grafi/degreeGest.json",'w') as file:
   json.dump(degree,file)

print("name,degree,indeg,outdg,cent")
for elem in degree:
   print(str(elem)+','+str(degree[elem]["degree"])+','+str(degree[elem]['Indegree'])+','+str(degree[elem]['Outdegree'])+','+str(cent[elem]))
