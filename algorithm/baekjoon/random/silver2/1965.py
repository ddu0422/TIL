import sys

n = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))
d = [1] * 1000

for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
