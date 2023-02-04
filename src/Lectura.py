# Clase que lee los archivos de texto
class Lectura:

    def __init__(self):
        pass

    def read_weighted_graph(self, file_path):
        graph = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if not line.startswith('#'):
                        vertex1, vertex2, weight = line.split()
                        if vertex1 not in graph:
                            graph[vertex1] = {}
                        graph[vertex1][vertex2] = float(weight)
            return graph
        except:
            print("path not found")