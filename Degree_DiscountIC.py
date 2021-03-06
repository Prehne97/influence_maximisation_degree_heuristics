__author__='https://github.com/nd7141/influence-maximization/blob/b57dc02f8019334c20fcc3d8236c19c287d98d2c/IC/degreeDiscount.py'

''' Implementation of degree discount heuristic [1] for Independent Cascade model
of influence propagation in graph G

[1] -- Wei Chen et al. Efficient influence maximization in Social Networks (algorithm 4)
'''
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import random 
from priorityQueue import PriorityQueue as PQ

def degreeDiscountIC(G, k,p=.05):
    ''' Finds initial set of nodes to propagate in Independent Cascade model (with priority queue)
    Input: G -- networkx graph object
    k -- number of nodes needed
    p -- propagation probability
    Output:
    S -- chosen k nodes
    '''
    S = []
    dd = PQ() # degree discount
    t={}
    d={}

    # initialize degree discount
    for u in G.nodes():
        d[u] = sum([G[u][v]['weight'] for v in G[u]]) # each edge adds degree 1
        # d[u] = len(G[u]) # each neighbor adds degree 1
        dd.add_task(u, -d[u]) # add degree of each node
        t[u] = 0

    # add vertices to S greedily
    for i in range(k):
        u, priority = dd.pop_item() # extract node with maximal degree discount
        S.append(u)
        for v in G[u]:
            if v not in S:
                t[v] += G[u][v]['weight'] # increase number of selected neighbors
                priority = d[v] - 2*t[v] - (d[v] - t[v])*t[v]*p    
                dd.add_task(v, -priority)
    return S

def degreeDiscountStar(G,k,p=.01):
    
    S = []
    scores = PQ()
    d = dict()
    t = dict()
    for u in G:
        d[u] = sum([G[u][v]['weight'] for v in G[u]])
        t[u] = 0
        score = ((1-p)**t[u])*(1+(d[u]-t[u])*p)
        scores.add_task(u,-score )
    for iteration in range(k):
        u, priority = scores.pop_item()
        S.append(u)
        for v in G[u]:
            if v not in S:
                t[v] += G[u][v]['weight']
                score = ((1-p)**t[v])*(1+(d[v]-t[v])*p)
                scores.add_task(v, -score)
    return S
            
