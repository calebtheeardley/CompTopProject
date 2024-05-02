from Edge import Edge
from Vertex import Vertex

class Graph:

    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.vertices = vertices
        self.edges = edges