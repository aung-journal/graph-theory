# This is NP hard on other graphs but on DAG, it can be solved
# in O(V+E)

#You just have have to multiply all edge values by -1 and find the shortest path
# and multiply edge values by -1 again

from setup import nx, dag_edges_2, create_dag
from shortest_dag import dagShortestPath
import json

def dagLongestPath(dag_edges, start: int):
    dag_edges = [(u, v, weight * -1) for u, v, weight in dag_edges]
    g = create_dag(dag_edges)
    return {node: weight*-1 for node, weight in dagShortestPath(g, start).items()}

# Test the function with the start node 1
def main():
    print(dagLongestPath(dag_edges_2, 1))
    with open('ans.json', 'a') as f:
        json.dump(dagLongestPath(dag_edges_2, 1), f)

if __name__ == '__main__':
    main()