import networkx as nx

def load_graph(dataset = "musae"):
##########################
# edge list should be a list with touple in it
# dtype:   (int or str  , int or str  ,  float)
# example: [(node,node,weight),(node,node,weight)]
##########################
    if dataset == "musae":
        edge = []
        with open('./musae_facebook.csv','r') as f:  
            data = f.readlines()  
            for line in data[2:]:
                line = tuple(line.replace('\r','').replace('\n','').replace('\t','').split(','))
                line = (line[0],line[1],float(line[4]))
                edge.append(line)
        edge= edge[1:]
        edge
        G1 = nx.Graph()
        G1.add_weighted_edges_from(edge)
        print("nodes:",G1.number_of_nodes())
        print("edges:",G1.number_of_edges())
        print(G1.number_of_nodes)
        G_neighbor1=  {}
        for node in G1.nodes():
            neighbors = []
            for node1 in nx.neighbors(G1,node):
                neighbors.append(node1)
            G_neighbor1[node] = neighbors
        print("ego-facbook data load successful")
        print("clustering coefficient:",nx.average_clustering(G1))
        return G1
    if dataset == "ego":
        edge2 = []
        with open('./ego_facebook.txt','r') as f2:  
            data2 = f2.readlines()  
            for line in data2:
                line = tuple(line.replace('\r','').replace('\n','').replace('\t','').split(' '))
                line = (int(line[0]),int(line[1]),1.0)
                edge2.append(line)
                
        G2 = nx.Graph()
        G2.add_weighted_edges_from(edge2)
        print("nodes:",G2.number_of_nodes())
        print("edges:",G2.number_of_edges())
        G_neighbor2=  {}
        for node in G2.nodes():
            neighbors = []
            for node1 in nx.neighbors(G2,node):
                neighbors.append(node1)
            G_neighbor2[node] = neighbors
        print("ego-facbook data load successful")
        print("clustering coefficient:",nx.average_clustering(G2))
        return G2
    if dataset == "wiki":
        edge4 = []
        with open('./wiki-Vote.txt','r') as f4:  
            data3 = f4.readlines() 
            for line in data3[4:]:
                line = tuple(line.replace('\n','').split())
                line = (int(line[0]),int(line[1]),1.0)
                edge4.append(line)
                
        G4 = nx.Graph()
        G4.add_weighted_edges_from(edge4)
        print("nodes:",G4.number_of_nodes())
        print("edges:",G4.number_of_edges())
        G_neighbor4=  {}
        for node in G4.nodes():
            neighbors = []
            for node1 in nx.neighbors(G4,node):
                neighbors.append(node1)
            G_neighbor4[node] = neighbors
        print("wiki data successful")
        print("clustering coefficient:",nx.average_clustering(G4))
        return G4

