def factorial(num):
    if num>1:
        return num * factorial(num-1)
    else:
        return num
'''
for num in range(10):
    print(factorial(num))
'''
#재귀함수를 활용해서 1부터 num까지의 곱이 출력되게 만드세요
def factorial_product(num):
    if num <=1:
        return num
    else:
        return num* factorial_product(num-1)

print(factorial_product(5))

#재귀함수를 이용한 리스트의 합
def sum_list(data):
    if len(data)<=1:
        return data[0]
    return data[0]+sum_list(data[1:])

data=[1,2,3,4,5,6,7,8,9,10]
print(sum_list(data))

#회문 검사. 첫글자와 마지막 글자가 같으면 회문 검사 첫 조건은 만족. 그 안쪽 글자도
#회문의 조건을 만족하는지 재귀를 통해서 검사한다.
def palindrome(string):
    if len(string)<=1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome("level"))