import sys

sys.setrecursionlimit(130000)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)


for edge in edges:
    edge.sort()


def dfs(r, depth):
    visited[r] = depth

    for v in edges[r]:
        if visited[v] == -1:
            dfs(v, visited[r] + 1)


dfs(r, 0)
print(*visited[1:], sep="\n")
