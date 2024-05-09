from Graph import Graph
from Edge import Edge
from Vertex import Vertex
import random as R

def parse_graph(source: str,width: int) -> Graph:
    vertices: list[Vertex] = []
    edges: list[Edge] = []  

    #TODO: Parse Vertices

    with open(source+"Vertice_ID.csv") as file:
        position = ""
        for line in file:
            data: list = line.removesuffix("\n").removesuffix(",").split(",")[:2]

            if(data[0] == "Sinks"):
                position = "Sinks"
            elif(data[0] == "Sources"):
                position = "Sources"

            if(len(data) > 1):
                if(position == "Sinks"):
                    vertices.append(Vertex(id=data[1],label=data[0], type="SINK", width=width))
                elif(position == "Sources"):
                    vertices.append(Vertex(id=data[1],label=data[0], type="SOURCE", width=width))
            

    with open(source+"CandidateNetwork.txt") as file:
        next(file)
        for line in file:
            data: list = line.split()[:3]

            v1: Vertex = next(filter(lambda v: v.label == data[0], vertices), None)
            v2: Vertex = next(filter(lambda v: v.label == data[1], vertices), None)
            if(not v1):
                v1 = Vertex(id="", label=data[0], type="NONE", width=width)
                vertices.append(v1)
            if(not v2):
                v2 = Vertex(id="", label=data[1], type="NONE", width=width)
                vertices.append(v2)

            weight: float = float(data[2])
            edge: Edge = Edge(vertices=(v1,v2), weight=weight)
            v1.neighbors.append(v2)
            v2.neighbors.append(v1)
            edges.append(edge)

    vertices = list(set(vertices))
    edges = list(set(edges))

    return Graph(vertices=vertices, edges=edges)

def parse_solution_graph(source: str, originalsource:str, width: int) -> Graph:
    baseGraph: Graph = parse_graph(source=originalsource, width=width)

    vertices: list[Vertex] = []
    edges: list[Edge] = []  

    with open(source) as file:
        atEdges = False
        for line in file:
            data: list = line.removesuffix("\n").removesuffix(",").split(",")
            if(not atEdges):
                if(data[0] == "Edge Source"):
                    atEdges = True
                continue

            v1: Vertex = next(filter(lambda v: v.label == data[0], baseGraph.vertices), None)
            v2: Vertex = next(filter(lambda v: v.label == data[1], baseGraph.vertices), None)
            edge = Edge((v1,v2), float(data[2]))
            vertices.append(v1)
            vertices.append(v2)
            edges.append(edge)

    vertices = list(set(vertices))
    edges = list(set(edges))

    return Graph(vertices=vertices, edges=edges)