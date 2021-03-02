import sys

n = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().rstrip().split()))[:n]
m = max(scores)
new_scores = [score / m * 100 for score in scores]
average = sum(new_scores) / n

print(average)
