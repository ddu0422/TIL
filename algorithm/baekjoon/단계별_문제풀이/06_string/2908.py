import sys

num1, num2 = sys.stdin.readline().rstrip().split()
print(max(int(num1[::-1]), int(num2[::-1])))
