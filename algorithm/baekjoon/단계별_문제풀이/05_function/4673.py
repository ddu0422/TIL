size = 10001


def d(n):
    return n + add_digits(n)


def add_digits(number):
    result = 0

    while number:
        result += number % 10
        number //= 10

    return result


counts = [0] * size

for i in range(1, size):
    self_number = d(i)
    if self_number < size:
        counts[self_number] += 1

for i in range(1, size):
    if counts[i] == 0:
        print(i)
