import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)


queue = deque([1])
visited[1] = 1

while queue:
    x = queue.popleft()

    for v in edges[x]:
        if not visited[v]:
            queue.append(v)
            visited[v] = visited[x] + 1


print(visited.count(2) + visited.count(3))
