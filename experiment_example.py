import time
from tqdm import tqdm
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import random 

from priorityQueue import PriorityQueue as PQ
from Degree_DiscountIC import  degreeDiscountIC 
from Second_Neighbour_Expected_Influence import SecondNeighbourDegreeDiscountIC
from runIC import runIC





edge_wiki=[]                                               # Load a dataset 
with open('wiki-Vote.txt','r') as f4:
    data4 = f4.readlines()  
    for line in data4[4:]:
        line = tuple(line.replace('\r','').replace('\n','').split())
        line = (int(line[0]),int(line[1]),1.0)
        edge_wiki.append(line)
    
G_wiki=nx.Graph()
G_wiki.add_weighted_edges_from(edge_wiki)
print("nodes:",G_wiki.number_of_nodes())
print("edges:",G_wiki.number_of_edges())
G_neighbor_wiki=  {}
for node in G_wiki.nodes():
	neighbors = []
	for node1 in nx.neighbors(G_wiki,node):
		neighbors.append(node1)
	G_neighbor_wiki[node] = neighbors

p=0.02   # set propagation probability

inf_old_different_k = []                       # influence of S from degree dicount                     
time_old_different_k = []                      # time taken
for k in tqdm([5,10,15,20,25,30,35,40,45,50,55,60,65,70]):
    time1 = time.time()
    s = degreeDiscountIC(G_wiki,k,False,G_neighbor_wiki,p)
    algorithm_time = time.time()
    inf = 0
    R= 2000
    Rancas_time = time.time()
    for i in range(R):
        t=runIC(G_wiki,s,p)
        inf = inf+len(t)
    inf = inf/R
    t1 = time.time()-Rancas_time
    inf_old_different_k.append(inf)
    time_old_different_k.append(algorithm_time-time1)
    
    
    
inf_new_different_k = []     # influence of S from second neighbour method
time_new_different_k = []


for k in tqdm([5,10,15,20,25,30,35,40,45,50,55,60,65,70]):
    time1 = time.time()
    s =SecondNeighbourDegreeDiscountIC(G_wiki,k,G_neighbor_wiki,p)
    algorithm_time = time.time()
    inf = 0
    R= 2000
    results=runIC(G_wiki,s,p)
    Rancas_time = time.time()
    for i in range(R):
        t=runIC(G_wiki,s,p)
        inf = inf+len(t)
     
    inf = inf/R
    t1 = time.time()-Rancas_time
    inf_new_different_k.append(inf)
    time_new_different_k.append(algorithm_time-time1)
    
    
    
    
print(inf_old_different_k)
print(time_old_different_k)
print(inf_new_different_k)
print(time_new_different_k)
    
    
    
    
    
    
    
