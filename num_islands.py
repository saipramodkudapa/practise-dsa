from typing import List
from collections import defaultdict


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        graph = Graph()

        nr, nc = len(grid), len(grid[0])

        def is_valid(tup):
            i, j = tup
            return (0 <= i < nr and 0 <= j < nc and grid[i][j] == '1')

        def gen_key(tup):
            i, j = tup
            return str(i) + '-' + str(j)

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    graph.add_vertice(gen_key((i, j)))
                    possible_dest = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    for dest in possible_dest:
                        if is_valid(dest):
                            graph.add_edge(gen_key((i, j)), gen_key(dest))

        # graph.print_graph()
        return graph.dfs()


class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_vertice(self, source):
        self.adj_list[source] = []

    def add_edge(self, source, dest):
        self.adj_list[source].append(dest)

    def print_graph(self):
        print(self.adj_list)
        print(self.adj_list.keys())

    def dfs(self):
        visited = set()
        res = 0

        def dfs_util(source, visited):
            stack = []
            stack.append(source)

            while stack:
                curr = stack.pop()

                if curr not in visited:
                    # visit curr
                    # print(curr)
                    visited.add(curr)

                for neighbour in self.adj_list[curr]:
                    if neighbour not in visited:
                        stack.append(neighbour)

        for vertice in self.adj_list:
            if vertice not in visited:
                res += 1
                dfs_util(vertice, visited)
        return res


