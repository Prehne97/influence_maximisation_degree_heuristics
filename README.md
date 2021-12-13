# influence_maximisation_degree_heuristics
Repository for SNACS research project involving degree heuristics  for the influence maximization problem.

## abstract
Influence maximization is the problem of finding a small subset of
nodes, referred to as seed nodes, in a social network that together
could maximize the spread of influence. In this paper, we investigate the degree discount method of Chen et al. [1] and derive a
novel algorithm that incorporates second neighbour effects, for the
independent cascade model. Our experimental results show that
our improved algorithm achieves competitive runtimes, due to its
complexity of O(𝑚+𝑛 log𝑛+𝑘 log2 𝑛), and achieves better influence
spread than the classic degree discount method of Chen et al. [1].
Importantly we show that expected influence calculations beyond
direct neighbours are indeed manageable using combinatorics, contrary to what was implied in [1]. Based on our new theory and
results, we believe that our Second Neighbours Expected Influence
heuristics may compete with current state of the art methods, as 𝑘
increases
![Alt text](https://github.com/Prehne97/influence_maximisation_degree_heuristics/blob/main/prob2.PNG =1000)

## Prerequisites

- Python 3.7
- matplotlib
- numpy
- tqdm
- networkx

## Datasets
ego-facebook:`http://snap.stanford.edu/data/ego-Facebook.html`

musae-facebook:`http://snap.stanford.edu/data/facebook-large-page-page-network.html`

wikipidia -vote:`https://snap.stanford.edu/data/wiki-Vote.html`

## Run Experiments(8 hours on Apple M1)
run 

`python main.py --experiment=True`

## Run only our new method(15 minutes on Apple M1)
run 

`python main.py --experiment=False`  

## reference
[1] Wei Chen, Yajun Wang, and Siyu Yang. 2009. Efficient Influence Maximization in
Social Networks. In Proceedings of the 15th ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining (Paris, France) (KDD ’09). Association
for Computing Machinery, New York, NY, USA, 199–208. https://doi.org/10.
1145/155701
