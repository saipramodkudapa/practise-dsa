
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

    def is_cyclic(self):
        in_stack, visited = {}, set()

        def dfs_util(source, visited, in_stack):
            visited.add(source)
            in_stack[source] = True

            for neighbour in self.adj_list[source]:
                if in_stack.get(neighbour, False):
                    return True
                elif neighbour not in visited and dfs_util(neighbour, visited, in_stack):
                    return True
            in_stack[source] = False
            return False

        for vertex in self.adj_list.keys():
            if dfs_util(vertex, visited, in_stack):
                return True
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)

g.print_graph()

print(g.is_cyclic())

