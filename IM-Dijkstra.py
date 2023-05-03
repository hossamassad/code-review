import heapq
from typing import List, Tuple, Dict, Union


def dijkstra_shortest_path(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> Union[None, Tuple[List[str], int]]:
    """
    Finds the shortest path from the start node to the end node in a graph using Dijkstra's algorithm.

    Args:
        graph: A dictionary representing the graph in adjacency list format.
        start: The start node.
        end: The end node.

    Returns:
        A tuple containing the shortest path from the start node to the end node as a list of nodes, and the cost of the
        shortest path. Returns None if there is no valid path from the start node to the end node.
    """
    heap = [(0, start)]
    visited = set()
    previous_node = {start: None}
    costs = {start: 0}

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            path = []
            while current is not None:
                path.insert(0, current)
                current = previous_node[current]
            return (path, cost)

        for neighbor, edge_cost in graph[current]:
            new_cost = costs[current] + edge_cost

            if neighbor not in visited and (neighbor not in costs or new_cost < costs[neighbor]):
                heapq.heappush(heap, (new_cost, neighbor))
                costs[neighbor] = new_cost
                previous_node[neighbor] = current

    return None
