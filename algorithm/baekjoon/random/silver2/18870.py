import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
deduplication_number = sorted(list(set(numbers)))
score = {deduplication_number[i] : i for i in range(len(deduplication_number))}

for i in numbers:
    print(score[i], end=' ')
print()
