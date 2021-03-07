import sys

text = sys.stdin.readline().rstrip()
counts = [-1] * 26

for i, s in enumerate(text):
    index = ord(s) - ord('a')
    if counts[index] == -1:
        counts[index] = i

for count in counts:
    print(count, end=" ")
