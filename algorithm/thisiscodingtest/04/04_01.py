import sys

n = int(sys.stdin.readline().rstrip())
commands = sys.stdin.readline().rstrip().split()


def first_solution(n, commands):
    x, y = 1, 1

    for command in commands:
        nx, ny = x, y

        if command == 'R':
            ny = y + 1
        elif command == 'L':
            ny = y - 1
        elif command == 'U':
            nx = x - 1
        elif command == 'D':
            nx = x + 1

        if not (0 < nx <= n and 0 < ny <= n):
            continue

        x, y = nx, ny

    print(x, y)


first_solution(n, commands)


def second_solution(n, commands):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for command in commands:
        for i in range(len(move_types)):
            if command == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if not (0 < nx <= n and 0 < ny <= n):
            continue

        x, y = nx, ny

    print(x, y)


second_solution(n, commands)
