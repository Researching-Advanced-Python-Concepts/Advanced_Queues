from custom_queue.queues import Queue
from queue_usage.graph import (
    City,
    load_graph,
)


def is_20th_century(city):
    return city.year and 1901 <= city.year <= 2000


def breadth_first_traverse(graph, source):
    queue = Queue(source)
    visited = {source}
    while queue:
        # our queue is iterable by dequeuing elements using
        # a for loop also
        yield (node := queue.dequeue())
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)


def breadth_first_search(graph, source, predicate):
    print()
    # City(name='Edinburgh', country='Scotland', year=1329,
    # latitude=55.953333, longitude=-3.189167)
    print("source is: ", source)
    print()
    for node in breadth_first_traverse(graph, source):
        # loop over the yielded nodes
        if predicate(node):
            print()
            # City(name='Lancaster', country='England',
            # year=1937, latitude=54.047, longitude=-2.801)
            print(node)
            print()
            return node


if __name__ == "__main__":
    nodes, graph = load_graph("queue_usage/roadmap.dot", City.from_dict)
    city = breadth_first_search(graph, nodes["edinburgh"], is_20th_century)
    print(city.name)

    print()
    for city in breadth_first_traverse(graph, nodes["edinburgh"]):
        print(city.name)
