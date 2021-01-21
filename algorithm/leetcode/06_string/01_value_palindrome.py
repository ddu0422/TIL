from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자열, 숫자만을 필터링한 후 소문자로 변환(숫자는 무시됨)
        text = deque([c.lower() for c in s if c.isalnum()])

        # 짝수인 경우 전부 같아야하고, 홀수인 경우 가운데 언제나 옳기 때문에 무시해도 된다.
        while len(text) > 1:
            # 처음과 마지막을 꺼내서 확인한다.
            if text.popleft() != text.pop():
                # 처음과 마지막이 다르면 False
                return False
                # 나머지 경우 True
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
