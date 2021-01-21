from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 식별자 이후 문자열 비교 사전순 정렬, 숫자는 입력 순으로 정렬
        letters, numbers = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                numbers.append(log)

        # 문자가 동일할 경우 식별자 기준으로 사전순 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + numbers


logs = [
    "dig1 8 1 5 1", "let1 art can", "dig2 3 6",
    "let2 own kit dig", "let3 art zero"
]

print(Solution().reorderLogFiles(logs))
