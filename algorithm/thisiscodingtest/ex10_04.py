"""
입력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력
159
"""
# 사전 준비
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

edges = []
result = 0

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

# 문제 풀이
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parnet(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parnet(parent, a, b)
    result += cost

print(result)