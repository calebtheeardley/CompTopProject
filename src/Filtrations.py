import numpy as np
from Graph import Graph
from Vertex import Vertex
from Edge import Edge

def maxWeight(graph: Graph) -> float:
    max_edge: Edge = max(graph.edges, key=lambda edge: edge.weight)
    return max_edge.weight

def vietros_rips_filtration_0_1(graph: Graph, div:int = 4, path: str = "none" ) -> list[set]:
    print("filtering")
    filtration: list[set] = []

    F: Graph = Graph([],[])
    max = int(maxWeight(graph=graph))

    i = 0
    for threshhold in range(0,max,int(max/100)):
        if(threshhold%int(max/100) == 0):
            print(str(i)+"%")
            i += 1

        for edge in graph.edges:
            if(edge.weight <= threshhold) :
                F.edges.append(edge)
                F.vertices.append(edge.vertices[0])
                F.vertices.append(edge.vertices[1])

        F.vertices = list(set(F.vertices))
        F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
        
        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)

        division: int = (max//div)
        if(threshhold%division <= int(max/100)):
            if(path != "none"):
                F.save(path+str(threshhold)+".png")

    return filtration

def vietros_rips_filtration_0_1_2(graph: Graph) -> list[set]:
    print("filtering")
    filtration: list[set] = []

    F: Graph = Graph([],[])
    max = int(maxWeight(graph=graph))

    i = 0
    for threshhold in range(0,max,int(max/100)):
        if(threshhold%int(max/100) == 0):
            print(str(i)+"%")
            i += 1

        for edge in graph.edges:
            if(edge.weight <= threshhold) :
                F.edges.append(edge)
                F.vertices.append(edge.vertices[0])
                F.vertices.append(edge.vertices[1])

        F.vertices = list(set(F.vertices))
        F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
        
        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)

        for edge in F.edges:
            v1 = edge.vertices[0]
            v2 = edge.vertices[1]
            

            for v3 in F.vertices:
                if(v1 != v3 and v2 != v3):
                    edge1_3 = next(filter(lambda edge: set(edge.vertices) == set([v1,v3]), F.edges), None)
                    edge2_3 = next(filter(lambda edge: set(edge.vertices) == set([v2,v3]), F.edges), None)
                    if(edge1_3 and edge2_3):
                        simplex2: set = set([v1,v2,v3])
                        if(simplex2 not in filtration):
                            filtration.append(simplex2)


        # quarter_point: int = (max//4)
        # if(threshhold%quarter_point <= int(max/100)):
        #     F.print()

    return filtration