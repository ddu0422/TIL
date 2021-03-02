import sys

numbers = []
for _ in range(9):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

max_value = 0
current_index = 0

for i in range(len(numbers)):
    if max_value < numbers[i]:
        max_value = numbers[i]
        current_index = i

print(max_value)
print(current_index + 1)
