import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
result = []

first = 0
second = 0

while first < n and second < m:
    if a[first] > b[second]:
        result.append(b[second])
        second += 1
    elif a[first] < b[second]:
        result.append(a[first])
        first += 1
    else:
        result.append(a[first])
        first += 1

if first < n:
    result += a[first:]
elif second < m:
    result += b[second:]

print(*result, sep=" ")
