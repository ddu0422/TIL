import sys

text = sys.stdin.readline().rstrip()


def palindrome(text):
    if text == text[::-1]:
        return len(text)
    
    for i in range(len(text)):
        temp_text = text + text[:i + 1][::-1]
        if temp_text == temp_text[::-1]:
            return len(text) + i + 1
    
    return len(text) * 2 + 1


print(palindrome(text))
