__author__='https://github.com/Prehne97'


import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import random 

from priorityQueue import PriorityQueue as PQ


def prob_function(p,t_v,T_v):
  '''
  Calculates the probability of a node v not being activated by its t_v direct seed neighbours and T_v seed second neighbours


  '''
    f=1-p
    if t_v==0:
        if T_v==0:
           return 1
        else:
           prob= 1-p**2
           if T_v==1:
               return prob
           else:
               for i in range(2,T_v+1):
                   prob= prob - p*p*((1-p*p)**(i-1))
               return prob

    else:                 # there are direct neighbours
        prob= f**t_v        # just the t_v probability (star(v) only)
        if T_v==0:
            return prob        
        else:
            prob= prob - prob*p*p
            if T_v==1:
                return prob
            else:
                for i in range(2,T_v+1):
                        prob = prob - p*p*f*f* ((1-p*p)**(i-1))
                return prob

def SecondNeighbourDegreeDiscountIC(G, k,neighbor_dict, p=.01,):
    ''' Finds initial set of nodes to propagate in Independent Cascade model (with priority queue) incorporating second neighbour effects
    Input: G -- networkx graph object
    k -- number of nodes needed
    p -- propagation probability
    Output:
    S -- chosen k nodes
    '''
    S = []
    sdd = PQ() # degree discount
    
    d = dict() # degree of each vertex
    delta = dict() # total number of vertices a distance of 2 away 

    t = dict() # number of adjacent vertices that are in S
    T = dict() # number of vertices a distance of 2 away that are in S
    P = dict() # probabilities that node won't be activted by surrounding seeds


    # initialize degree discount
    for u in G.nodes():
        d[u] = sum([G[u][v]['weight'] for v in G[u]]) # each edge adds degree 1
        t[u] = 0
        T[u] = 0
        P[u] = 1
    for u in G.nodes():   # sum up the total number of second neighbours of a node 
      count_second = 0
      for v in G[u]:
        if d[v]>0:
          count_second += (d[v] -1)

      delta[u] = count_second

    for u in G.nodes():
        # d[u] = len(G[u]) # each neighbor adds degree 1
        s_score= (1+ d[u]*p + delta[u]*(p**2))
        sdd.add_task(u, -s_score) # add degree of each node


    # add vertices to S greedily
    for i in range(k):
        u, priority = sdd.pop_item() # extract node with maximal degree discount
        S.append(u)
        for v in neighbor_dict[u]:
            if v not in S:
                t[v] += G[u][v]['weight'] # increase number of selected neighbors
                s_score= prob_function(p,t[v],T[v])*( p*(d[v] - t[v]) +  ((p**2)*(delta[v] - T[v]))  )
                sdd.add_task(v, -s_score)
                for w in neighbor_dict[v]:
                  if w not in S:
                    T[w]=T[w]+1
                    s_score= prob_function(p,t[w],T[w])*( p*(d[w] - t[w]) +  ((p**2)*(delta[w] - T[w]))  )
                    sdd.add_task(w, -s_score)





                
                
    return S
