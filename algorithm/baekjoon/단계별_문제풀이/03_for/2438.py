import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(0, i + 1):
        print("*", end="")
    print()
