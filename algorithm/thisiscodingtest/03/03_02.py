import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))[:n]

# 시간 복잡도: O(nlogn), n은 배열의 크기 ->> 내림차순으로 정렬
numbers = sorted(numbers, reverse=True)
second_largest_number_count = m % k
largest_number_count = m - second_largest_number_count

print(
    numbers[0] * largest_number_count +
    numbers[1] * second_largest_number_count
)
