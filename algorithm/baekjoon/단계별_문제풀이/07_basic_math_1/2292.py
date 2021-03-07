"""
1 -> (제외) 0 취급
6
12
18

A(n + 1) = 6A(n) (n >= 2)
S(n) = ((n - 1) * 6) * n // 2
입력값 <= 3n^2 - 3n + 1
-> 그 때의 n을 구하기
"""
import sys

n = int(sys.stdin.readline().rstrip())

index = 1

while True:
    if n <= 3 * index * index - 3 * index + 1:
        break
    index += 1

print(index)
