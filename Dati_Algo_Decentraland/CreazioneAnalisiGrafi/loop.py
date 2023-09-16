import matplotlib
import json
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from networkx.readwrite import json_graph
with open("../Dati/Dati_Grafi/graphfilereal.json","r") as file:
   data2=json.load(file)
G = json_graph.node_link_graph(data2)
print(G)
result1=sorted(nx.strongly_connected_components(G),key=len)
