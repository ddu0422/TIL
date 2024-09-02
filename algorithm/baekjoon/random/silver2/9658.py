import sys

n = int(sys.stdin.readline().rstrip())
d = [False] * (n + 5)

# False: 창영이 우승, True: 상근이 우승
d[1] = False
d[2] = True
d[3] = False
d[4] = True

for i in range(5, n + 1):
    if d[i - 1] and d[i - 3] and d[i - 4]:
        d[i] = False
    else:
        d[i] = True

print("SK" if d[n] else "CY")
