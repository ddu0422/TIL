import sys

n = int(sys.stdin.readline().rstrip())
position = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    position.append((x, y))

position.sort(key=lambda x: x[0])

# 루프탑(가장 높은 기둥) 찾기 
roof_top = max(position, key=lambda x: x[1])
# 루프탑 후보
max_index = [i for i, value in enumerate(position) if value[1] == roof_top[1]]

# 루프탑 기준으로 왼편, 오른편
left_max_index, right_max_index = min(max_index), max(max_index)
left, right = position[:left_max_index + 1], position[right_max_index:][::-1]

# 왼편, 오른편 면적 계산
def calculate(array):
    if not array:
        return 0

    sum = 0
    max_value = array[0][1]

    for i in range(len(array) - 1):
        sum += max_value * abs(array[i + 1][0] - array[i][0])
        if array[i][1] < array[i + 1][1]:
            max_value = max(max_value, array[i + 1][1])

    # 기둥 배열 + 루프탑까지 면적 계산
    return sum


print(
    # 왼편 + 루프탑 사이 + 오른편
    calculate(left) + (position[right_max_index][0] - position[left_max_index][0] + 1) * roof_top[1] + calculate(right)
)
