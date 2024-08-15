from collections import defaultdict, deque

"""
    using adjaceny list 

    adjacency list is where we store all vertices in a hashmap where each vertex store its neighbours
"""


class Edge:
    def __init__(self, src, dest, weight) -> None:
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph:
    def __init__(self, is_directed=False) -> None:
        self.adj_list = defaultdict(list)
        self.is_directed = is_directed

    def add_vertex(self, v):
        self.adj_list[v] = []

    def add_edge(self, src, dest, weight=0):
        if src not in self.adj_list:
            raise ValueError("Index  not present")
        if dest not in self.adj_list:
            raise ValueError("Destination vertex not present")
        self.adj_list[src].append((dest, weight))
        if not self.is_directed:
            self.adj_list[dest].append((src, weight))

    def bfs(self, node):
        """
        TC : O(V) --> for travelling each vertex using while loop
        O(E) --> for iterating over all neighbors

        TC:- O(V+E)
        """
        queue = deque([node])
        seen = set()

        while queue:
            current = queue.popleft()
            if current not in seen:
                print(current, end=" ")
                seen.add(current)
            for neighbor, _ in self.adj_list[current]:
                if neighbor not in seen:
                    queue.append(neighbor)

        pass

    def dfs(self, node):
        """
        Time complexity:- O(V+E)

        """

        seen = set()

        def helper(vertex):
            if vertex not in seen:
                print(vertex, end=" ")
                seen.add(vertex)
                for i in self.adj_list[vertex]:
                    neighbor = i[0]
                    helper(neighbor)

        helper(node)

        pass


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)

    # Adding edges
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    print("BFS:")
    graph.bfs(1)  # Output: 1 2 3 4

    print("\nDFS:")
    graph.dfs(1)  # Output: 1 2 4 3
