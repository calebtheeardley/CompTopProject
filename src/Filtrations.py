import numpy as np
from Graph import Graph
from Vertex import Vertex
from Edge import Edge

def maxWeight(graph: Graph) -> float:
    max_edge: Edge = max(graph.edges, key=lambda edge: edge.weight)
    return max_edge.weight


def vietros_rips_filtration(graph: Graph, div:int = 4, path: str = "none" ) -> tuple[list[set],dict]:
    print("filtering")
    filtration: list[set] = []
    threshold_dict: dict = {}

    F: Graph = Graph([],[])
    max = int(maxWeight(graph=graph))

    i = 0
    stepsize = 1
    threshold = 0

    while(threshold <= max):

        fsize = len(F.edges)+len(F.vertices)
        gsize = len(graph.edges)+len(graph.vertices)
        percent_done = fsize*100/gsize
        print(str(percent_done)+"%")

        for edge in graph.edges:
            if(edge.weight <= threshold) :
                F.edges.append(edge)
                F.vertices.append(edge.vertices[0])
                F.vertices.append(edge.vertices[1])

        F.vertices = list(set(F.vertices))
        F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
                threshold_dict[len(filtration)-1] = threshold
        
        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)
                threshold_dict[len(filtration)-1] = threshold
                

        for edge in F.edges:
            v1 = edge.vertices[0]
            v2 = edge.vertices[1]
            
            for v3 in F.vertices:
                if(v1 in v3.neighbors and v2 in v3.neighbors):
                    edge1_3 = next(filter(lambda edge: set(edge.vertices) == set([v1,v3]), F.edges), None)
                    edge2_3 = next(filter(lambda edge: set(edge.vertices) == set([v2,v3]), F.edges), None)
                    if(edge1_3 and edge2_3):
                        simplex2: set = set([v1,v2,v3])
                        if(simplex2 not in filtration):
                            filtration.append(simplex2)
                            threshold_dict[len(filtration)-1] = threshold
                        
        threshold += stepsize
        division: int = (max//div)
        if(threshold%division < stepsize or threshold == 1):
            if(path != "none"):
                F.save(path+str(threshold)+".png", "threshold = "+str(threshold))

    for i in range(len(filtration)+1):
        if(i not in threshold_dict):
            threshold_dict[i] = threshold_dict[i-1]

    return (filtration, threshold_dict)


def my_filtration_source(graph: Graph, path: str="none") -> tuple[list[set], dict]:
    sources: list[Vertex] = []
    filtration: list[set] = []
    threshold_dict: dict = {}

    F: Graph = Graph([],[])

    for V in graph.vertices:
        if(V.type == "SOURCE"):
            sources.append(V)
            F.vertices.append(V)
            filtration.append(set([V]))
    
    for i in range(len(filtration)+1):
        threshold_dict[i] = 0

    threshold = 1
    stepsize = 1
    repeats = 0
    percent_done = 0
    
    while(len(F.vertices) < len(graph.vertices) and (percent_done < 97 or repeats > 5)):
        
        fsize = len(F.edges)+len(F.vertices)
        gsize = len(graph.edges)+len(graph.vertices)
        percent_done = fsize*100/gsize
        print(str(percent_done)+"%")

        startsize: int = len(filtration)
        for source in sources:
            for edge in graph.edges:
                if(edge not in F.edges and edge.weight<=threshold):
                    if(threshold > 500):
                        a=0
                    dist: float = graph.dijkstra_shortest_path(source, edge)
                    if(dist <= threshold):
                        F.edges.append(edge)
                        F.vertices.append(edge.vertices[0])
                        F.vertices.append(edge.vertices[1])
                
            F.vertices = list(set(F.vertices))
            F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
                threshold_dict[len(filtration)-1] = threshold
   

        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)
                threshold_dict[len(filtration)-1] = threshold

        for edge in F.edges:
            v1 = edge.vertices[0]
            v2 = edge.vertices[1]
            
            for v3 in F.vertices:
                if(v1 in v3.neighbors and v2 in v3.neighbors):
                    edge1_3 = next(filter(lambda edge: set(edge.vertices) == set([v1,v3]), F.edges), None)
                    edge2_3 = next(filter(lambda edge: set(edge.vertices) == set([v2,v3]), F.edges), None)
                    if(edge1_3 and edge2_3):
                        simplex2: set = set([v1,v2,v3])
                        if(simplex2 not in filtration):
                            filtration.append(simplex2)
                            threshold_dict[len(filtration)-1] = threshold

        endsize: int = len(filtration)
        if(startsize == endsize):
            repeats += 1
            stepsize *= 1.2
        else:
            repeats = 0
            if(path != "none"):
                F.save(path+str(threshold)+".png", "threshold = "+str(threshold))

        threshold += int(stepsize)

    
    for i in range(len(filtration)+1):
        if(i not in threshold_dict):
            threshold_dict[i] = threshold_dict[i-1]
    return(filtration, threshold_dict)

def my_filtration_sink(graph: Graph, path: str="none") -> tuple[list[set], dict]:
    sinks: list[Vertex] = []
    filtration: list[set] = []
    threshold_dict: dict = {}

    F: Graph = Graph([],[])

    for V in graph.vertices:
        if(V.type == "SINK"):
            sinks.append(V)
            F.vertices.append(V)
            filtration.append(set([V]))
    
    for i in range(len(filtration)+1):
        threshold_dict[i] = 0

    threshold = 1
    stepsize = 3
    repeats = 0
    percent_done = 0
    
    while(len(F.vertices) < len(graph.vertices) and percent_done < 97):
        
        fsize = len(F.edges)+len(F.vertices)
        gsize = len(graph.edges)+len(graph.vertices)
        percent_done = fsize*100/gsize
        print(str(percent_done)+"%")

        startsize: int = len(filtration)
        for sink in sinks:
            for edge in graph.edges:
                if(edge not in F.edges and edge.weight<=threshold):
                    if(threshold > 500):
                        a=0
                    dist: float = graph.dijkstra_shortest_path(sink, edge)
                    if(dist <= threshold):
                        F.edges.append(edge)
                        F.vertices.append(edge.vertices[0])
                        F.vertices.append(edge.vertices[1])
                
            F.vertices = list(set(F.vertices))
            F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
                threshold_dict[len(filtration)-1] = threshold
   

        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)
                threshold_dict[len(filtration)-1] = threshold

        for edge in F.edges:
            v1 = edge.vertices[0]
            v2 = edge.vertices[1]
            
            for v3 in F.vertices:
                if(v1 in v3.neighbors and v2 in v3.neighbors):
                    edge1_3 = next(filter(lambda edge: set(edge.vertices) == set([v1,v3]), F.edges), None)
                    edge2_3 = next(filter(lambda edge: set(edge.vertices) == set([v2,v3]), F.edges), None)
                    if(edge1_3 and edge2_3):
                        simplex2: set = set([v1,v2,v3])
                        if(simplex2 not in filtration):
                            filtration.append(simplex2)
                            threshold_dict[len(filtration)-1] = threshold

        endsize: int = len(filtration)
        if(startsize == endsize):
            repeats += 1
            stepsize *= 1.2
        else:
            repeats = 0
            if(path != "none"):
                F.save(path+str(threshold)+".png", "threshold = "+str(threshold))

        threshold += int(stepsize)

    

    return(filtration, threshold_dict)

def discrete_morse_filtration(graph: Graph, path: str="none") -> tuple[list[set], dict]:
    filtration: list[set] = []
    threshold_dict: dict = {}

    #Discrete Morse Function
    for edge in graph.edges:
        v1, v2 = edge.vertices
        if(v1.weight == None and v2.weight == None):
            edge.weight = 2
            v1.weight = 1
            v2. weight = 3
        elif(v1.weight == None):
            edge.weight = v2.weight + 1
            v1.weight = edge.weight + 1
        elif(v2.weight == None):
            edge.weight = v1.weight + 1
            v2.weight = edge.weight + 1
        elif(v1.weight == v2.weight):
            edge.weight = v1.weight + 1
        else:
            edge.weight = (v1.weight + v2.weight)/2
    
    for V in graph.vertices:
        if(V.weight == None):
            V.weight = 0

    max = int(maxWeight(graph=graph))
    F: Graph = Graph([],[])
    stepsize = 1
    for threshold in range(0, max, stepsize):
        fsize = len(F.edges)+len(F.vertices)
        gsize = len(graph.edges)+len(graph.vertices)
        percent_done = fsize*100/gsize
        print(str(percent_done)+"%")

        for V in graph.vertices:
            if(V.weight <= threshold):
                F.vertices.append(V)
        for E in graph.edges:
            if(E.weight <= threshold):
                F.edges.append(E)
                F.vertices.append(E.vertices[0])
                F.vertices.append(E.vertices[1])
        F.vertices = list(set(F.vertices))
        F.edges = list(set(F.edges))

        for vertex in F.vertices:
            simplex0: set = set([vertex])
            if(simplex0 not in filtration):
                filtration.append(simplex0)
                threshold_dict[len(filtration)] = threshold
   

        for edge in F.edges:
            simplex1: set = set([edge.vertices[0], edge.vertices[1]])
            if(simplex1 not in filtration):
                filtration.append(simplex1)
                threshold_dict[len(filtration)] = threshold

        for edge in F.edges:
            v1 = edge.vertices[0]
            v2 = edge.vertices[1]
            
            for v3 in F.vertices:
                if(v1 in v3.neighbors and v2 in v3.neighbors):
                    edge1_3 = next(filter(lambda edge: set(edge.vertices) == set([v1,v3]), F.edges), None)
                    edge2_3 = next(filter(lambda edge: set(edge.vertices) == set([v2,v3]), F.edges), None)
                    if(edge1_3 and edge2_3):
                        simplex2: set = set([v1,v2,v3])
                        if(simplex2 not in filtration):
                            filtration.append(simplex2)
                            threshold_dict[len(filtration)-1] = threshold

        if(path != "none"):
            F.save(path+str(threshold)+".png", "threshold = "+str(threshold))

    for i in range(len(filtration)+1):
        if(i not in threshold_dict):
            threshold_dict[i] = threshold_dict[i-1]

    return(filtration, threshold_dict)
    
