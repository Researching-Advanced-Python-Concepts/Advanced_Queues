# Breadth First Search


import networkx as nx
from queue_usage.graph import City, load_graph


def is_20th_century(year):
    return year and 1901 <= year <= 2000


def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude,
                       reverse=True))


if __name__ == "__main__":
    nodes, graph = load_graph("queue_usage/roadmap.dot",
                              City.from_dict)
    for node in nx.bfs_tree(graph, nodes["edinburgh"]):
        # look at breadth first before going down a node
        print("📍", node.name)
        if is_20th_century(node.year):
            print("Found:", node.name, node.year)
            break
    else:
        print("Not found")

    print()
    print("Sorted order")
    for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
        # look at breadth first before going down a node
        print("📍", node.name)
        if is_20th_century(node.year):
            print("Found:", node.name, node.year)
            break
    else:
        print("Not found")
