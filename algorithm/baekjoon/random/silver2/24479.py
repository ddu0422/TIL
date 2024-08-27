import sys

sys.setrecursionlimit(130000)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)


for edge in edges:
    edge.sort()

index = 1

def dfs(r):
    global index
    visited[r] = index

    for v in edges[r]:
        if not visited[v]:
            index += 1
            visited[v] = index
            dfs(v)

dfs(r)
print(*visited[1:], sep="\n")
