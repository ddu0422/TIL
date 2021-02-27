import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print(n, "*", i, "=", n * i)
