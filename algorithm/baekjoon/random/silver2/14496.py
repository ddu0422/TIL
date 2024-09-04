import sys
from collections import deque

a, b = map(int, sys.stdin.readline().rstrip().split())
n, m = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)


queue = deque([a])
distance[a] = 1

while queue:
    c = queue.popleft()

    for v in edges[c]:
        if not distance[v]:
            distance[v] = distance[c] + 1
            queue.append(v)

    print(distance)

print(distance[b] - 1)
