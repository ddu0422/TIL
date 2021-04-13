from collections import defaultdict


def solution(participant, completion):
    answer = ''
    dictionary = defaultdict(int)

    for name in participant:
        dictionary[name] += 1

    for name in completion:
        dictionary[name] -= 1

    for key, value in dictionary.items():
        if value == 1:
            answer = key
            break

    return answer
