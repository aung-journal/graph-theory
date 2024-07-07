from setup import nx, plt, Union, bf_edges_2, bf_edges_1

def visualize_weight_graph(G: Union[nx.Graph, nx.DiGraph]):
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray', width=2, style='dotted')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.show()

g = nx.DiGraph()
for u, v, w in bf_edges_1:
    g.add_edge(u, v, weight=w)
visualize_weight_graph(g)