from typing import List, Optional

class Vertex:
    def __init__(self, data: str) -> None:
        self.data: str = data
        self.edges: List[Edge] = []
    
    def add_edge(self, dest: 'Vertex', weight: Optional[int]) -> None:
        edge = Edge(self, dest, weight)
        self.edges.append(edge)
    
    def remove_edge(self, dest: 'Vertex') -> None:
        self.edges = [edge for edge in self.edges if edge.dest != dest]
    
    def get_data(self) -> str:
        return self.data
    
    def get_edges(self) -> List['Edge']:
        return self.edges
    
    def print(self, display_weight: bool) -> None:
        if not self.edges:
            print(f"{self.data} -->")
            return 
        message = ""
        for i, edge in enumerate(self.edges):
            if i == 0:
                message += f"{edge.src.data} --> "
            message += f"{edge.dest.data}" 
            if display_weight:
                message += f" ({edge.weight})"
            if i != len(self.edges) - 1:
                message += ","
            message += '\n'
        print(message)


class Edge:
    def __init__(self, src: Vertex, dest: Vertex, weight: Optional[int]) -> None:
        self.src: Vertex = src
        self.dest: Vertex = dest
        self.weight: Optional[int] = weight

    def get_src(self) -> Vertex:
        return self.src 
    
    def get_dest(self) -> Vertex:
        return self.dest

    def get_weight(self) -> Optional[int]:
        return self.weight    

class Graph:

    def __init__(self, is_weighted: bool, is_directed: bool) -> None:
        self.vertices: List[Vertex] = []
        self.directed: bool = is_directed
        self.weighted: bool = is_weighted

    def add_vertex(self, data: str) -> Vertex:
        vertex = Vertex(data)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight: Optional[int]) -> None:
        if not self.weighted:
            weight = None
        
        vertex1.add_edge(vertex2, weight)

        if not self.directed:
            vertex2.add_edge(vertex1, weight)

    def remove_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        vertex1.remove_edge(vertex2)
        if not self.directed:
            vertex2.remove_edge(vertex1)

    def remove_vertex(self, vertex: Vertex) -> None:
        self.vertices.remove(vertex)

    def get_vertices(self) -> List[Vertex]:
        return self.vertices

    def get_is_weighted(self) -> bool:
        return self.weighted
    
    def get_is_directed(self) -> bool:
        return self.directed
    
    def get_vertex_by_value(self, value: str) -> Optional[Vertex]:
        for vertex in self.vertices:
            if vertex.data == value:
                return vertex
        return None

    def print(self, is_weighted: bool) -> None:
        for vertex in self.vertices:
            vertex.print(is_weighted)

if __name__ == "__main__":

    bus_network = Graph(True, False)

    kakinada_station = bus_network.add_vertex("kakinada")
    tenali_station = bus_network.add_vertex("tenali")
    
    bus_network.add_edge(kakinada_station, tenali_station, 300)
    bus_network.print(bus_network.get_is_weighted())
