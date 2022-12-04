from typing import NamedTuple
import networkx as nx

filename = "queue_usage/roadmap.dot"


def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )


class City(NamedTuple):
    # inheriting so that node objects are hashable
    # can access with dot notation
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        """Takes a dict of attributes extracted from a DOT file
        and return a new instance of city class
        """
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )


def sort_by(neighbors, strategy):
    # City(name='Bath', country='England', year=1090,
    # latitude=51.38, longitude=-2.36):
    # {'distance': '115', 'label': '115'} -> neighbors
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))


def by_distance(weights):
    return float(weights["distance"])


if __name__ == "__main__":
    nodes, graph = load_graph(filename, City.from_dict)
    print("nodes")
    print(nodes)
    print()
    print("graph")
    print(graph)

    print()
    for neighbour in graph.neighbors(nodes["london"]):
        print(neighbour.name)

    print()
    print("graph nodes london")
    print(graph[nodes["london"]])
    print()
    print("neighbour with their distance")
    for neighbour, weights in graph[nodes["london"]].items():
        print(neighbour.name, weights["distance"])

    print()
    print("neighbour with their distance, sorted")
    for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
        # 3 place ahead
        print(f"{weights['distance']:>3} miles", neighbor.name)
