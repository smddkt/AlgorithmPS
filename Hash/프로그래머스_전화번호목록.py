#전화번호부에 적힌 전화번호를 담은 배열이 solution 함수의 매개변수로 주어질 때, 
#어떤 번호가 다른 번호의 접두어인 경우 false를, 접두어가 아니면 true를 리턴하는 solution 함수.

# 정렬(sort)을 이용한 풀이
def solution(phone_book):
    result = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] ==phone_book[i]:
                answer = False
                break
    return answer


#해시를 이용한 풀이

def solution(phone_book):
    phone_book_dict = {}

    for phone_number in phone_book:
        phone_book_dict[phone_number] = True

    for phone_number in phone_book:
        temp = ""
        for char in phone_number:
            temp += char
            if temp in phone_book_dict and temp != phone_number:
                return False
    
    return True