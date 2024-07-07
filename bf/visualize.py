from setup import nx, bf_edges_2, visualize_graph

g = nx.DiGraph()
g.add_edges_from(bf_edges_2)
visualize_graph(g)