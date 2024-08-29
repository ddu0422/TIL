import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
sharks = deque([])
maps = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    lines = list(map(int, sys.stdin.readline().rstrip().split()))
    for y, value in enumerate(lines):
        if value == 1:
            sharks.append((x, y))
    maps.append(lines)


def bfs():
    while sharks:
        cx, cy = sharks.popleft()
        
        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if maps[nx][ny] == 0:
                maps[nx][ny] = maps[cx][cy] + 1
                sharks.append((nx, ny))


bfs()
max_value = 0

for x in range(n):
    for y in range(m):
        max_value = max(max_value, maps[x][y])

print(max_value - 1)
