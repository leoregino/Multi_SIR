# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import hashlib 

# This is just a hash for debbugind and display purposes
def compute_cheap_hash(txt , length = 4):
    
    hash.hashlib.sha1()
    hash.update(txt)
    return hash.hexdigest()[:length]


#############################################
### 1. Preprocessing the initial CSV File ###
#############################################

# Local path to CSV
local_path_csv = r'C:\Users\Leonardo REGINO\Documents\Projectos Perso\Modelos SIR\Files\Data_set\Localidad_Usaquen_Edges_20210131.csv'

data = pd.read_csv(local_path_csv)

df = pd.DataFrame(data, columns = [ 'id1' ,'id2' ] )


df['weight'] = 1 


#### For debbuging and displaying purposes ####
df['id1'] = df['id1'].apply(lambda x : x[0:4]) 
df['id2'] = df['id2'].apply(lambda x : x[0:4]) 

df = df.drop_duplicates()

### Select 1 node to display all its connections 
df_single_node = df[df["id1"] == "0012"]

### 2. Load graph from edges df ###
G = nx.from_pandas_edgelist(df_single_node,'id1','id2')


# show graph general info 
print("Number of nodes: " + str(G.number_of_nodes())) 
print("------")

print("Number of edges: " + str(G.number_of_edges()))
print("------")


## todo : 1. Sample graph 

nodes_sample = df["id1"].sample(2)

G_sub = G.subgraph(nodes_sample)

# Plot graph 
nx.draw(G, with_labels=True)
plt.savefig("Simple_path.png") # save as PNG
plt.show() # display



## todo : 2. Calculate centrality measurements per node 
degrees = nx.degree_centrality(G)
katz = nx.katz_centrality(G)
closeness = nx.closeness_centrality(G)
betweeness = nx.betweenness_centrality(G)
eigs = nx.eigenvector_centrality(G)


### Assemble 

df_centr = pd.DataFrame([degrees, katz, closeness, betweeness, eigs]).transpose()

df_centr.columns = ['degrees', 'katz', 'closeness', 'betweeness', 'eigs']



