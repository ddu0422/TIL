import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))[:n]

for number in a:
    if number < x:
        print(number, end=" ")
