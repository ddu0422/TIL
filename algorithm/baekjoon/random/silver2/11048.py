import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
d = [[0] * m for _ in range(n)]
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            d[i][j] = a[i][j]
            continue

        if i == 0:
            d[i][j] = d[i][j - 1] + a[i][j]
            continue

        if j == 0:
            d[i][j] = d[i - 1][j] + a[i][j]
            continue

        d[i][j] = max(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + a[i][j]

print(d[n - 1][m - 1])
