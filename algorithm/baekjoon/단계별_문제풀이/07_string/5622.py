import sys

text = sys.stdin.readline().rstrip()
times = [
    3, 3, 3,
    4, 4, 4,
    5, 5, 5,
    6, 6, 6,
    7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9,
    10, 10, 10, 10
]

answer = 0

for s in text:
    answer += times[ord(s) - ord('A')]

print(answer)
