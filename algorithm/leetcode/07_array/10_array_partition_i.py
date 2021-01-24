from typing import List

# 두 수를 선택해 작은 값을 정한다.
# 해당 수들을 더했을 때 최댓값을 구한다.
# 즉, 두 수의 차이를 줄여야한다.

# 해결방법
# 오름차순으로 정렬한다.
# 두 수를 선택해 작은 수를 선택한다.
# 더한다.


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            answer += min(nums[i], nums[i + 1])

        return answer
