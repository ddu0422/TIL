import sys

count = int(sys.stdin.readline().rstrip())
result = 0


def is_group_checker(text):
    checker = [False] * 26

    for i in range(len(text) - 1):
        checker[ord(text[i]) - ord('a')] = True

        if text[i] == text[i + 1]:
            continue

        if checker[ord(text[i + 1]) - ord('a')]:
            return False

    return True


for _ in range(count):
    text = sys.stdin.readline().rstrip()
    result += 1 if is_group_checker(text) else 0

print(result)
