from collections import Counter


def solution(clothes):
    answer = 1
    counts = Counter([cloth[1] for cloth in clothes])

    for value in counts.values():
        answer *= (value + 1)

    return answer - 1
