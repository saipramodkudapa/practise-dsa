import math
import collections
import functools
mines = [(1.0, 2.0, 3), (2.0, 1.0, 2)]


def euclidean(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


graph = collections.defaultdict(list)
for i in range(len(mines)):
    x1, y1, br1 = mines[i]
    for j in range(len(mines)):
        x2, y2, br2 = mines[j]
        if i != j and euclidean(x1, y1, x2, y2) <= br1:
            graph[(x1, y1)].append((x2, y2))


@functools.lru_cache(maxsize=None)
def dfs(source, blasted):
    blasted.add(source)
    max_neighbor = 0
    for neighbor in graph[source]:
        if neighbor not in blasted:
            max_neighbor = max(max_neighbor, dfs(neighbor, blasted))

    return 1 + max_neighbor


res = 0
for mine in mines:
    blasted = set()
    res = max(res, dfs(mine, blasted))

print(res)