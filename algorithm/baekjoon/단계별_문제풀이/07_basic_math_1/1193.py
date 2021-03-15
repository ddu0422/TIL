import sys

x = int(sys.stdin.readline().rstrip())
n = 1


def total(n):
    return (n * (n + 1)) // 2


while total(n) < x:
    n += 1

difference = total(n) - x

print(
    f"{n - difference}/{1 + difference}" if n % 2 == 0
    else f"{1 + difference}/{n - difference}"
)
