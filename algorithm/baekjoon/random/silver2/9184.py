import sys

number = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return number[20][20][20]
    
    if a < b and b < c:
        return number[a][b][c - 1] + number[a][b - 1][c - 1] - number[a][b - 1][c]
    
    return number[a - 1][b][c] + number[a - 1][b - 1][c] + number[a - 1][b][c - 1] - number[a - 1][b - 1][c - 1]


for i in range(21):
    for j in range(21):
        for k in range(21):
            number[i][j][k] = w(i, j, k)


while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())

    if a == -1 and  b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
