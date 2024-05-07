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
            
    # with open(source+"Sinks.csv", "r", newline='') as file:
    #     next(file)
    #     for line in file:
    #         data: list = line.removesuffix("\n").removesuffix(",").split(",")[:12]
    #         id: str = data[0]
    #         type: str = "SINK"
    #         x: int = int(float(data[10]))
    #         y: int = int(float(data[11]))

    #         V: Vertex = next(filter(lambda v: [v.id, v.type] == [id, type], vertices), None)
    #         V.pos = (x,y)

    # with open(source+"Sources.csv", "r", newline='') as file:
    #     next(file)
    #     for line in file:
    #         data: list = line.removesuffix("\n").removesuffix(",").split(",")[:9]
    #         id: str = data[0]
    #         type: str = "SOURCE"
    #         x: int = int(float(data[7]))
    #         y: int = int(float(data[8]))

    #         V: Vertex = next(filter(lambda v: [v.id, v.type] == [id, type], vertices), None)
    #         V.pos = (x,y)
    

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
            edges.append(edge)

    # string_vertices: list[tuple[str,str]] = []
    # with open(vertex_file, "r") as file:
    #     for line in file:

    #         data: list = line.split()[:4]
    #         if(data[0] != "#"):
    #             string_vertices.append((data[1],data[0]))
    #             string_vertices.append((data[3],data[2]))
    # string_vertices = list(set(string_vertices))

    # for v in string_vertices:
    #     id: str = v[0]
    #     type: str = v[1]
    #     # pos: tuple[int] = (int(id[:4]),int(id[3:]))
    #     pos: tuple[int] = (R.randint(0,100),R.randint(0,100))
    #     if(id == None):
    #         continue

    #     vertices.append(Vertex(id=int(id),pos=pos,type=type))

    # #TODO: Parse Edges
    # with open(edge_file, "r") as file:
    #     for line in file:

    #         data: list = line.split()
    #         data_edge: list = data[:4]

    #         if(data_edge[0] == "Vertex1"):
    #             continue
    #         else:
    #             v1: Vertex = next(filter(lambda v: v.id == int(data[0]), vertices), None)
    #             v2: Vertex = next(filter(lambda v: v.id == int(data[1]), vertices), None)
    #             if(not v1):
    #                 # pos: tuple[int] = (int(data[0][:4]),int(data[0][3:]))
    #                 pos: tuple[int] = (R.randint(0,100),R.randint(0,100))
    #                 v1 = Vertex(id=int(data[0]), pos=pos, type="none")
    #                 vertices.append(v1)
    #             if(not v2):
    #                 # pos: tuple[int] = (int(data[1][:4]),int(data[1][3:]))
    #                 pos: tuple[int] = (R.randint(0,100),R.randint(0,100))
    #                 v2 = Vertex(id=int(data[1]), pos=pos, type="none")
    #                 vertices.append(v2)

    #             weight: float = float(data[3])
    #             edge: Edge = Edge(vertices=(v1,v2), weight=weight)
    #             edges.append(edge)

    #TODO: Create Graph

    vertices = list(set(vertices))
    edges = list(set(edges))

    return Graph(vertices=vertices, edges=edges)