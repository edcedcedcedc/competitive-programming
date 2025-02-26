import networkx as nx
import matplotlib.pyplot as plt

def draw_relation_graph(relation, elements, title="Relation Graph"):
    """Draws a directed graph for a given relation."""
    G = nx.DiGraph()
    G.add_nodes_from(elements)
    G.add_edges_from(relation)
    
    # Layout for a better visual appearance
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', arrows=True)
    plt.title(title)
    plt.show()

# Example relation
elements = {1, 2, 3, 4}
relation = {(1, 2), (2, 3), (3, 4), (1, 3), (2, 4)}  # Example directed edges

# Draw the graph
draw_relation_graph(relation, elements, title="Directed Graph of the Relation")
