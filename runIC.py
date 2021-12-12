__author__='https://github.com/nd7141/influence-maximization/blob/b57dc02f8019334c20fcc3d8236c19c287d98d2c/IC/degreeDiscount.py'

import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import random 

def runIC (G, S, p = .01):
    ''' Runs independent cascade model.
    Input: G -- networkx graph object
    S -- initial set of vertices
    p -- propagation probability
    Output: T -- resulted influenced set of vertices (including S)
    '''
    T = deepcopy(S) # copy already selected nodes
    # random.seed(2)
    # ugly C++ version
    i = 0
    while i < len(T):
        for v in G[T[i]]: # for neighbors of a selected node
            if v not in T: # if it wasn't selected yet
                w = G[T[i]][v]['weight'] # count the number of edges between two nodes
                if random.random() <= 1 - (1-p)**w: # if at least one of edges propagate influence
                    #print (T[i], 'influences', v)
                    T.append(v)
        i += 1
    return T
