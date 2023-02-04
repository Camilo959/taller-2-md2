import heapq

# Clase que recibe un diccionario y encuentra el camino
# más corto entre dos vertices usando el algoritmo de Dijkstra
class Dijkstra:

    def __init__(self) -> None:
        pass

    def dijkstra(self, graph, start, end):
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0
        queue = [(0, start)]
        previous_vertices = {vertex: None for vertex in graph}
        while queue:
            (current_distance, current_vertex) = heapq.heappop(queue)
            if current_vertex == end:
                return (distances[end], self.path(previous_vertices, start, end))
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))
        return float('infinity'), []

    def path(self,previous_vertices, start, end):
        if end is None:
            return []
        return self.path(previous_vertices, start, previous_vertices[end]) + [end]