import sys

n = sys.stdin.readline().rstrip()
original = int(n)
result = 0

while True:
    if len(n) == 1:
        n = "0" + n
        
    a, b = n
    next_value = str(eval("{} + {}".format(a, b)))
    n = b + str(int(next_value) % 10)
    result += 1
    
    if original == int(n):
        break


print(result)