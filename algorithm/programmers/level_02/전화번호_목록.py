def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            answer = False
            break

    return answer
