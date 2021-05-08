import sys

n = int(sys.stdin.readline().rstrip())


def repeat_text(text, n):
    return text * n


for _ in range(n):
    count, text = sys.stdin.readline().rstrip().split()

    for s in text:
        print(repeat_text(s, int(count)), end="")
    print()
