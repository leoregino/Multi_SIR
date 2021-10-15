# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

### 1. Preprocessing the initial CSV File ###

# Local path to CSV
local_path_csv = r'C:\Users\Leonardo REGINO\Documents\Projectos Perso\Modelos SIR\Files\Data_set\Localidad_Usaquen_Edges_20210130.csv'

data = pd.read_csv(local_path_csv)

df = pd.DataFrame(data, columns = [ 'id1' ,'id2' ] )

df['weight'] = 1 


### 2. Load graph from edges df ###

G = nx.from_pandas_edgelist(df,'id1','id2')


# Plot graph 
nx.draw(G, with_labels=True)
plt.savefig("Simple_path.png") # save as PNG
plt.show() # display

## todo : 1. Sample graph 
## todo : 2. Calculate centrality measurements


