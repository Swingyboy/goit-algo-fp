import heapq
from typing import Dict


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = {}
        self.vertices[from_vertex][to_vertex] = weight

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def delete_edge(self, from_vertex: str, to_vertex: str) -> None:
        if from_vertex in self.vertices:
            if to_vertex in self.vertices[from_vertex]:
                del self.vertices[from_vertex][to_vertex]

    def delete_vertex(self, vertex: str) -> None:
        if vertex in self.vertices:
            del self.vertices[vertex]
            for edges in self.vertices.values():
                if vertex in edges:
                    del edges[vertex]

    @classmethod
    def from_dict(cls, graph_dict: Dict[str, Dict[str, int]]) -> 'Graph':
        graph = cls()
        for from_vertex, edges in graph_dict.items():
            for to_vertex, weight in edges.items():
                graph.add_edge(from_vertex, to_vertex, weight)
        return graph

    def to_dict(self) -> Dict[str, Dict[str, int]]:
        return self.vertices

    def dijkstra(self, start: str) -> Dict[str, float]:
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


if __name__ == "__main__":
    graph_dict = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 4, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    graph = Graph.from_dict(graph_dict)
    start_vertex = 'A'
    shortest_paths = graph.dijkstra(start_vertex)
    print(f"The sortest way from {start_vertex}: {shortest_paths}")
