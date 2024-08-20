import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
result = 1

while a < b:
    if b % 10 == 1:
        b //= 10
        result += 1
        continue

    if b % 2 == 0:
        b //= 2
        result += 1
        continue

    if b % 10 != 1:
        result = -1
        break

print(-1 if a > b else result)
