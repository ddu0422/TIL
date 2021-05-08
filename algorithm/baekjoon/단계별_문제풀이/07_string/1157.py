import sys

text = sys.stdin.readline().rstrip().upper()
counts = [0] * 26

for s in text:
    counts[ord(s) - ord('A')] += 1

max_value = max(counts)
result = 0
index = 0

for i, count in enumerate(counts):
    if max_value == count:
        result += 1
        index = i

if result > 1:
    print("?")
else:
    print(chr(index + ord('A')))
