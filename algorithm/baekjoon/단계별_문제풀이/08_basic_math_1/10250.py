import sys

t = int(sys.stdin.readline().rstrip())


def solution(height, width, n):
    floor = n % height if n % height else height
    ho = n // height + 1 if n % height else n // height

    if ho < 10:
        ho = str(0) + str(ho)

    return str(floor) + str(ho)


for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    print(solution(h, w, n))
