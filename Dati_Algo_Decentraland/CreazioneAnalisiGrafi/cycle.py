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
l=nx.number_of_selfloops(G)

print(l)
for e in nx.selfloop_edges(G):
   print(e)

with open("graphfilereal.json","r") as file:
   data2=json.load(file)
H = json_graph.node_link_graph(data2)
print(nx.number_of_selfloops(H))