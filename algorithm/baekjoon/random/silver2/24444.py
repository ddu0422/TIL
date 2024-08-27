import sys
from collections import deque

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
queue = deque([r])
visited[r] = index

while queue:
    x = queue.popleft()

    for v in edges[x]:
        if not visited[v]:
            index += 1
            visited[v] = index
            queue.append(v)

print(*visited[1:], sep="\n")
