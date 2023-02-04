# Clase que recibe un diccionario y encuentra el camino
# más corto entre dos vertices usando el algoritmo de Floyd
class Floyd:

    def __init__(self) -> None:
        pass

    def floyd(self, graph):
        vertices = list(graph.keys())
        distances = {vertex: {vertex2: float('inf') for vertex2 in vertices} for vertex in vertices}
        for vertex in vertices:
            distances[vertex][vertex] = 0
        for vertex1, neighbours in graph.items():
            for vertex2, weight in neighbours.items():
                distances[vertex1][vertex2] = weight
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
        return distances

    def get_shortest_path(self, distances, start, end):
        return distances[start][end]