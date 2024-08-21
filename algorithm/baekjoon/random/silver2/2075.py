import sys
import heapq

n = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    for number in numbers:
        if len(queue) < n:
            heapq.heappush(queue, number)
        else:
            if queue[0] < number:
                heapq.heappop(queue)
                heapq.heappush(queue, number)

print(queue[0])
