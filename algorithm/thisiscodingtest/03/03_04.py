import sys

n, k = map(int, sys.stdin.readline().rstrip().split())


def fisrt_solve(n, k):
    result = 0

    while n != 1:
        if (n % k == 0):
            n //= k
        else:
            n -= 1

        result += 1

    return result


print(fisrt_solve(n, k))


# 아래 방법도 알고 있기
def second_solve(n, k):
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target

        if n < k:
            break

        result += 1
        n //= k

    result += (n - 1)

    return result


print(second_solve(n, k))
