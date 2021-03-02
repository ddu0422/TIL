import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
result = str(a * b * c)
counts = [0] * 10

for digit in result:
    counts[digit] += 1

for count in counts:
    print(count)
