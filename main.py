import time
from tqdm import tqdm
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from priorityQueue import PriorityQueue as PQ
from Degree_DiscountIC import  degreeDiscountIC 
from Second_Neighbour_Expected_Influence import SecondNeighbourDegreeDiscountIC
from runIC import runIC
from data import load_graph
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--experiment",type = bool,   default =False)
args = parser.parse_args()
experiment = args.experiment

G = load_graph("ego")# "wiki""musae""ego"
k = 40
p=0.02   # set propagation probability
R = 2000
G_neighbor=  {}
for node in G.nodes():
	neighbors = []
	for node1 in nx.neighbors(G,node):
		neighbors.append(node1)
	G_neighbor[node] = neighbors

if experiment==False:
    time1 = time.time()
    s =SecondNeighbourDegreeDiscountIC(G,k,G_neighbor,p)
    algorithm_time = time.time()
    print("algorithm time: ", algorithm_time-time1)
    inf = 0
    Rancas_time = time.time()
    for i in tqdm(range(R)):
        t=runIC(G,s,p)
        inf = inf+len(t)
    inf = inf/R
    t1 = time.time()-Rancas_time
    print(R,"IC use time:",t1)
    print("average influence:",inf)
    

if experiment == True:
    inf_old_different_k = []                       # influence of S from degree dicount                     
    time_old_different_k = []                      # time taken
    for k in tqdm([5,10,15,20,25,30,35,40,45,50,55,60,65,70]):
        time1 = time.time()
        s = degreeDiscountIC(G,k,p)
        algorithm_time = time.time()
        inf = 0
        R= 2000
        Rancas_time = time.time()
        for i in tqdm(range(R)):
            t=runIC(G,s,p)
            inf = inf+len(t)
        inf = inf/R
        t1 = time.time()-Rancas_time
        inf_old_different_k.append(inf)
        time_old_different_k.append(algorithm_time-time1)
    inf_new_different_k = []     # influence of S from second neighbour method
    time_new_different_k = []
    for k in tqdm([5,10,15,20,25,30,35,40,45,50,55,60,65,70]):
        time1 = time.time()
        s =SecondNeighbourDegreeDiscountIC(G,k,G_neighbor,p)
        algorithm_time = time.time()
        inf = 0
        R= 2000
        results=runIC(G,s,p)
        Rancas_time = time.time()
        for i in tqdm(range(R)):
            t=runIC(G,s,p)
            inf = inf+len(t)
        inf = inf/R
        t1 = time.time()-Rancas_time
        inf_new_different_k.append(inf)
        time_new_different_k.append(algorithm_time-time1)
    inf_old_different_p = []
    time_old_different_p = []
    for p in tqdm([0.01,0.02,0.03,0.04,0.05]):
        time1 = time.time()
        s = degreeDiscountIC(G,40,p)
        algorithm_time = time.time()
        inf = 0
        R= 2000
        Rancas_time = time.time()
        for i in tqdm(range(R)):
            t=runIC(G,s,p)
            inf = inf+len(t)
        inf = inf/R
        t1 = time.time()-Rancas_time
        inf_old_different_p.append(inf)
        time_old_different_p.append(algorithm_time-time1)
    inf_new_different_p = []
    time_new_different_p = []        
    for p in tqdm([0.01,0.02,0.03,0.04,0.05]):
        time1 = time.time()
        s = SecondNeighbourDegreeDiscountIC(G,40,G_neighbor,p)
        algorithm_time = time.time()
        inf = 0
        R= 2000
        Rancas_time = time.time()
        for i in tqdm(range(R)):
            t=runIC(G,s,p)
            inf = inf+len(t)
        inf = inf/R
        t1 = time.time()-Rancas_time
        inf_new_different_p.append(inf)
        time_new_different_p.append(algorithm_time-time1)
    print("inf_old_different_k",inf_old_different_k)
    print("time_old_different_k",time_old_different_k)
    print('inf_new_different_k',inf_new_different_k)
    print('time_new_different_k',time_new_different_k)
    print('inf_old_different_p',inf_old_different_p)
    print('time_old_different_p',time_old_different_p)
    print("inf_new_different_p",inf_new_different_p)
    print("time_new_different_p",time_new_different_p)
    

    
    
    
    
