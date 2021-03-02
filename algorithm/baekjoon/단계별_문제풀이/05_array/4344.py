import sys

c = int(sys.stdin.readline().rstrip())

for _ in range(c):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    n, scores = data[0], data[1:]
    average = sum(scores) / n
    result = 0

    for score in scores:
        if score > average:
            result += 1

    print("{:.3f}%".format(result / n * 100))
