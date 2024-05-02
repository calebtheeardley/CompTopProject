from Vertex import Vertex

class Edge:

    def __init__(self, vertices: tuple[Vertex, Vertex], weight: float):
        self.vertices = vertices
        self.weight = weight
