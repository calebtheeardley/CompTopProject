from Edge import Edge
from Vertex import Vertex
import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np


class Graph:

    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.vertices = vertices
        self.edges = edges

    def print(self):
        G = nx.Graph() 
        vertices = []
        vertex_positions = {}
        vertex_colors = {}
        self.visual = []

        for v in self.vertices:
            vertices.append(v.label)


        for vertex in self.vertices:
            if(vertex.pos != None):
                vertex_positions[vertex.label] = np.array([vertex.pos[0],vertex.pos[1]])
            color: str = 'lightgrey'
            if(vertex.type == "SOURCE"):
                color = 'red'
            elif(vertex.type == "SINK"):
                color = 'blue'
            # else:
            #     color = 'black'
            vertex_colors[vertex.label] = color

        for edge in self.edges:
            e = [edge.vertices[0].label, edge.vertices[1].label, edge.weight]
            self.visual.append(e)
            

        G.add_weighted_edges_from(self.visual) 
        G.add_nodes_from(vertices)
        nx.draw_networkx(G, node_color=[vertex_colors.get(node) for node in G.nodes()], with_labels=False, pos=vertex_positions, node_size=50) 


        plt.show() 

    def save(self, path:str):
        G = nx.Graph() 
        vertices = []
        vertex_positions = {}
        vertex_colors = {}
        self.visual = []

        for v in self.vertices:
            vertices.append(v.label)


        for vertex in self.vertices:
            if(vertex.pos != None):
                vertex_positions[vertex.label] = np.array([vertex.pos[0],vertex.pos[1]])
            color: str = 'lightgrey'
            if(vertex.type == "SOURCE"):
                color = 'red'
            elif(vertex.type == "SINK"):
                color = 'blue'
            # else:
            #     color = 'black'
            vertex_colors[vertex.label] = color

        for edge in self.edges:
            e = [edge.vertices[0].label, edge.vertices[1].label, edge.weight]
            self.visual.append(e)
            

        G.add_weighted_edges_from(self.visual) 
        G.add_nodes_from(vertices)
        nx.draw_networkx(G, node_color=[vertex_colors.get(node) for node in G.nodes()], with_labels=False, pos=vertex_positions, node_size=50) 

        plt.savefig(path)
        