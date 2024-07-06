from setup import nx, plt, create, visualize, complex_graph, tree, complex_rooted_tree, undirected_edges, undirected_edges_3

G = create(complex_graph)
T = create(tree)
RT = create(complex_rooted_tree)

g = nx.Graph()
g.add_edges_from(undirected_edges_3)
#visualize(complex_rooted_tree)

def visualize_undirected_weight_graph(G: nx.Graph):
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray', width=2, style='dotted')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.show()

def visualize_undirected_weight_graph_2(G: nx.Graph):
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=50, font_size=5, font_weight='bold', edge_color='gray', width=2, style='dotted')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Undirected Weighted Graph with ~30 Nodes")
    plt.show()

visualize_undirected_weight_graph(g)