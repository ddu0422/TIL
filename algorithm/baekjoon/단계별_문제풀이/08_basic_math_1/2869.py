import sys

up, down, height = map(int, sys.stdin.readline().rstrip().split())


def calculate_days(up, down, height):
    # 마지막을 제외한 높이
    result = height - up
    # 하루에 올라간 높이
    difference = up - down

    # 하루에 올라간 높이가 전체 높이인 경우
    if result <= 0:
        return 1

    # 마지막에 올라갈 높이를 제외한 높이 + 마지막에 올라갈 높이
    if result % difference == 0:
        return result // difference + 1

    return result // difference + 2


print(calculate_days(up, down, height))
