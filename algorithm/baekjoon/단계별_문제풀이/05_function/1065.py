import sys

n = int(sys.stdin.readline().rstrip())


def is_hansu(number):
    if number < 10:
        return True

    numbers = list(map(int, str(number)))
    difference = numbers[0] - numbers[1]

    for i in range(1, len(numbers)):
        if difference != numbers[i - 1] - numbers[i]:
            return False

    return True


print(len([i for i in range(1, n + 1) if is_hansu(i)]))
