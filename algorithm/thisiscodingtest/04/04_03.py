import sys

location = sys.stdin.readline().rstrip()
x, y = int(location[1]), ord(location[0]) - ord('a') + 1
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

result = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)
