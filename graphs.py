import networkx as nx


# This is an empty graph with no vertex/node
G = nx.Graph()

G.add_node("Mike")  # add a single vertex

G.add_nodes_from(["Anne", "Bran", "Jon"])  # add bunch of vertices from a list

G.add_edge("Mike", "Anne")  # add one EDGE from existing vertices

print(G)
print(G.nodes)
print(G.edges)