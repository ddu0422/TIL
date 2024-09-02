import sys

d = [0] * (250 + 1)

d[0] = 1
d[1] = 1

for i in range(2, 251):
    d[i] = 2 * d[i - 2] + d[i - 1]

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        print(d[n])
    except:
        break