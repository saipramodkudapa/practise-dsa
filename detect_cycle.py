
class Graph:

    def __init__(self, num_vertices):
        self.adj_list = {}
        self.V = num_vertices
        for i in range(num_vertices):
            self.adj_list[i] = []

    def add_vertice(self, source):
        self.adj_list[source] = []

    def add_edge(self, source, dest):
        self.adj_list[source].append(dest)

    def print_graph(self):
        print(self.adj_list)
        print(self.adj_list.keys())

    def is_cyclic(self):
        colors = ['W']*self.V

        def dfs_util(source, colors):
            colors[source] = 'G'

            for neighbor in self.adj_list[source]:

                if colors[neighbor] == 'G':
                    return True

                elif colors[neighbor] == 'W' and dfs_util(neighbor, colors):
                    return True

            colors[source] = 'B'
            return False

        for vertex in self.adj_list.keys():
            if colors[vertex] == 'W' and dfs_util(vertex, colors):
                return True
        return False




g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(3, 0)
g.add_edge(5, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)


g.print_graph()

print(g.is_cyclic())

