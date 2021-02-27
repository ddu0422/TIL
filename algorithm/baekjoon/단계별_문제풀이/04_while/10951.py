import sys

# while 문제이지만 while구문으로 어떻게 푸는지 몰라 for문으로 풀었다.
for line in sys.stdin:
    a, b = map(int, line.rstrip().split())
    print(a + b)
