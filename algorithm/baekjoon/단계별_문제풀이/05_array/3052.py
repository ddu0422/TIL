import sys

numerator = 42
counts = [0] * numerator
numbers = []
for _ in range(10):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

for number in numbers:
    counts[number % numerator] += 1

print(len([count for count in counts if count > 0]))
