import sys

text = sys.stdin.readline().rstrip()
quack = 'quack'

def solution(text: str):
    if text[0] != "q" or text[-1] != "k" or len(text) % 5:
        return -1

    visited = [False] * len(text)
    result = 0

    for _ in range(len(text)):
        queue = []
        index = 0
        for i, v in enumerate(text):
            if visited[i]:
                continue

            if not queue and v == "q":
                queue.append(v)
                visited[i] = True
            elif queue and queue[-1] == quack[index % 5] and v == quack[(index + 1) % 5]:
                queue.append(v)
                visited[i] = True
                index += 1
        
        if len(queue) and len(queue) % 5 == 0:
            result += 1

    return result if result and all(visited) else -1


print(solution(text))
