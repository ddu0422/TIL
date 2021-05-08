import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    texts = sys.stdin.readline().rstrip()
    counts = [0] * len(texts)
    counts[0] = 1 if texts[0] == 'O' else 0

    for i in range(1, len(texts)):
        if texts[i] == 'O':
            counts[i] = counts[i - 1] + 1

    print(sum(counts))
