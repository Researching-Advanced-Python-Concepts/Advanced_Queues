import networkx as nx

# networkx is the fastest and most compliant with DOT format's
# advanced features
graph = nx.nx_agraph.read_dot("queue_usage/roadmap.dot")
print(graph)
print()
print(graph.nodes)
print()
print(graph.nodes["london"])
print()
# list of
# ('armagh', {'country': 'Northern Ireland', 'latitude': '54.3499',
# 'longitude': '-6.6546', 'pos': '7,74!', 'xlabel': 'Armagh',
# 'year': '1994'})
print(graph.nodes(data=True))
print()
# list of data like this:
# ('armagh', 'derry', {'distance': '61', 'label': '61'})
print(graph.edges(data=True))
print()


for name1, name2, weights in graph.edges(data=True):
    print(name1)
    print()
    print(name2)
    print()
    print(weights)
    print()
    # 2 nodes 1 edge
    print(nx.Graph([(name1, name2, weights)]*2))
    break


