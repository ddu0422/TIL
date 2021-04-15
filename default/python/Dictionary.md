### dictionary 란?

- Key와 Value의 쌍을 데이터로 가지는 자료형입니다.
- `변경 불가능한 데이터`를 키로 사용할 수 있습니다.
- 내부적으로 해시 테이블을 사용하며 검색 및 수정할 때 O(1)를 가집니다.
- `키는 중복 저장될 수 없지만`, `값은 중복 저장`될 수 있습니다.
- 저장된 키와 `동일한 키로` 값을 저장하면 기존의 값이 `새로운 값으로 대체`됩니다.
  <br/><br/>

```python
def solution():
    dictionary = dict()
    dictionary[0] = 1  # {0: 1}
    print(dictionary)
    dictionary[0] = 2  # {0: 2}
    print(dictionary)
    return

solution()
```

<br/>

### Dictionary가 제공하는 함수

|            함수            |                                                             설명                                                              |
| :------------------------: | :---------------------------------------------------------------------------------------------------------------------------: |
|     dict[key] = value      |                                                      해당 key에 값 할당                                                       |
|       del dict[key]        |                                         해당 key를 삭제, 키가 존재하지 않는다면 에러                                          |
|     key [not] in dict      |                                                         키 존재 여부                                                          |
|    get(key, [default])     |                      해당 key에 할당된 값을 반환, 키 값이 존재하지 않는다면 기본값으로 설정된 값을 반환                       |
|           keys()           |                                             dictionary에 존재하는 key 목록을 반환                                             |
|          values()          |                                            dictionary에 존재하는 value 목록을 반환                                            |
|          items()           |                                        dictionary에 존재하는 (key, value) 목록을 반환                                         |
| setdefault(key, [default]) | 해당 key에 할당된 값을 반환, 키 값이 존재하지 않는다면 기본값으로 설정된 값을 반환, get과 달리 dictionary의 key, value가 할당 |

<br/>

```python
def solution():
    dictionary = dict()
    print(dictionary.get(2, 3)) # 3
    print(dictionary.setdefault(3, 4)) # 4
    print(dictionary) # {3: 4}
    return

solution()
```

<br/>

### defaultdict

- collection module에 들어있습니다.
- defaultdict를 선언할 때 기본값으로 설정할 타입(callable object)을 넣으면 키가 존재하지 않을때 해당 값을 반환합니다.
  <br/><br/>

```python
from collections import defaultdict

def solution(participant, completion):
    answer = ''
    dictionary = defaultdict(int) # 키 값이 없으면 0으로 초기화

    for name in participant:
        dictionary[name] += 1 # 해당 키 값은 처음에 존재하지 않기 때문에 0에서 1을 더한 값을 저장

    for name in completion:
        dictionary[name] -= 1

    for key, value in dictionary.items():
        if value == 1:
            answer = key
            break

    return answer
```
