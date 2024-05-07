from Edge import Edge
from Vertex import Vertex
import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np
import heapq


class Graph:

    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = self._build_adjacency_list()

    def _build_adjacency_list(self):
        adjacency_list = {vertex.unique_id: [] for vertex in self.vertices}
        for edge in self.edges:
            start_vertex, end_vertex = edge.vertices
            adjacency_list[start_vertex.unique_id].append((end_vertex, edge.weight))
            adjacency_list[end_vertex.unique_id].append((start_vertex, edge.weight))  # Assuming the graph is undirected
        return adjacency_list

    def dijkstra_shortest_path(self, start_vertex, target_edge):
        distances = {vertex.unique_id: float('inf') for vertex in self.vertices}
        distances[start_vertex.unique_id] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if (current_vertex == target_edge.vertices[0] or current_vertex == target_edge.vertices[1]):
                # The target edge is reached
                return current_distance + target_edge.weight

            if (current_distance > distances[current_vertex.unique_id]):
                continue

            for neighbor, weight in self.adjacency_list[current_vertex.unique_id]:
                distance = current_distance + weight
                if (distance < distances[neighbor.unique_id]):
                    distances[neighbor.unique_id] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return float('inf')  # No path found

    def print(self):
        plt.close()
        G = nx.Graph() 
        vertices = []
        vertex_positions = {}
        vertex_colors = {}
        self.visual = []

        for v in self.vertices:
            vertices.append(v.unique_id)


        for vertex in self.vertices:
            if(vertex.pos != None):
                vertex_positions[vertex.unique_id] = np.array([vertex.pos[0],vertex.pos[1]])
            if(vertex.unique_id == "8367942_4"):
                a=0
            color: str = 'lightgrey'
            if(vertex.type == "SOURCE"):
                color = 'red'
            elif(vertex.type == "SINK"):
                color = 'blue'
            # else:
            #     color = 'black'
            vertex_colors[vertex.unique_id] = color

        for edge in self.edges:
            e = [edge.vertices[0].unique_id, edge.vertices[1].unique_id, edge.weight]
            self.visual.append(e)
            

        G.add_weighted_edges_from(self.visual) 
        G.add_nodes_from(vertices)
        nx.draw_networkx(G, node_color=[vertex_colors.get(node) for node in G.nodes()], with_labels=False, pos=vertex_positions, node_size=50) 


        plt.show() 

    def save(self, path:str, label: str = "none"):
        plt.close()
        G = nx.Graph() 
        vertices = []
        vertex_positions = {}
        vertex_colors = {}
        self.visual = []

        for v in self.vertices:
            vertices.append(v.unique_id)


        for vertex in self.vertices:
            if(vertex.pos != None):
                vertex_positions[vertex.unique_id] = np.array([vertex.pos[0],vertex.pos[1]])
            color: str = 'lightgrey'
            if(vertex.type == "SOURCE"):
                color = 'red'
            elif(vertex.type == "SINK"):
                color = 'blue'
            # else:
            #     color = 'black'
            vertex_colors[vertex.unique_id] = color

        for edge in self.edges:
            e = [edge.vertices[0].unique_id, edge.vertices[1].unique_id, edge.weight]
            self.visual.append(e)
            

        G.add_weighted_edges_from(self.visual) 
        G.add_nodes_from(vertices)
        nx.draw_networkx(G, node_color=[vertex_colors.get(node) for node in G.nodes()], with_labels=False, pos=vertex_positions, node_size=50) 
        if(label != "none"):
            plt.figtext(0.5, 0.01, label, ha="center", fontsize=12)

        plt.savefig(path, dpi=500)
        