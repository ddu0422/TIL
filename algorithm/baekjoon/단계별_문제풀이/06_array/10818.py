import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

min_value = min(numbers)
max_value = max(numbers)

print(min_value, max_value)
