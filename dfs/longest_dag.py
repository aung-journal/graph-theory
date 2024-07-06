# This is NP hard on other graphs but on DAG, it can be solved
# in O(V+E)

#You just have have to multiply all edge values by -1 and find the shortest path
# and multiply edge values by -1 again

from setup import nx, dag_edges
from shortest_dag import dagShortestPath

def dagLongestPath(dag_edges, start: int):
