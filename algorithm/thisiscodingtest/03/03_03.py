import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = []

# 시간 복잡도: O(n), n은 열의 크기 ->> 열과 행 중 큰 값
for _ in range(n):
    min_value = min(list(map(int, sys.stdin.readline().rstrip().split()))[:m])
    cards.append(min_value)

print(max(cards))
