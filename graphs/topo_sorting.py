
class Graph:

    def __init__(self, num_vertices):
        self.adj_list = {}
        for i in range(num_vertices):
            self.adj_list[i] = []

    def add_vertice(self, source):
        self.adj_list[source] = []

    def add_edge(self, source, dest):
        self.adj_list[source].append(dest)

    def print_graph(self):
        print(self.adj_list)
        print(self.adj_list.keys())

    def topo_order(self):

        def topo_util(source, visited, stack):
            visited.add(source)
            for neighbour in self.adj_list[source]:
                if neighbour not in visited:
                    topo_util(neighbour, visited, stack)
            stack.append(source)

        visited, stack = set(), []
        for vertex in self.adj_list.keys():
            if vertex not in visited:
                topo_util(vertex, visited, stack)
        stack.reverse()
        print(stack)


g = Graph(6)
g.add_edge(5, 0)
g.add_edge(5, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(4, 1)
g.add_edge(4, 0)

g.print_graph()

g.topo_order()

