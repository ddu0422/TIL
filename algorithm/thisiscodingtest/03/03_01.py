import sys

n = int(sys.stdin.readline().rstrip())

coins = [500, 100, 50, 10]
result = 0

# 시간 복잡도: O(k), k는 coin의 개수
for coin in coins:
    result += n // coin
    n %= coin

print(result)
