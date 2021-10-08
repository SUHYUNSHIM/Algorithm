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

##factorial2
#정수 n에 대해 n이 홀수면 3x n+1 을 하고
#n이 짝수면 n을 2로 나눈다.
#이렇게 계속 진행해서 n이 결국 1이 될 때까지 2,3의 과정을 반복합니다.
#예시 3 -> 3 10 5 16 8 4 2 1 이 출력.
#해당 함수를 작성하시오.
print("출력 시작")
def nums(n):
    if n == 1:
        return n
    else:
        if n%2 == 1:
            print(3*n+1)
            return(nums(3*n+1))
        elif n%2 == 0:
            print(int(n/2))
            return(nums(int(n/2)))
print(nums(3))
print("좀 더 깔끔하게, return 상태로 n을 저장한 뒤 처음 출력하는 아래의 방식이 맞다.")

def nums(n):
    print(n)
    if n == 1:
        return n
    else:
        if n%2 == 1:
            return(nums(3*n+1))
        elif n%2 == 0:
            return(nums(int(n/2)))
print(nums(3))

##factorial3
#n이 입력으로 주어졌을 떄,, n을 1,2,3의 합으로 나타낼 수 있는 방법을 구하시오
def sums(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    elif n==4:
        return sums(1)+sums(2)+sums(3)
    else:
        return 2*sums(n-1) ##앞 모든 것의 합이 아니라 앞의 3개까지의 합이라는 규칙이 있음!!
print(sums(6))

print("정답")
def func(data):
    if data ==1:
        return 1
    elif data ==2:
        return 2
    elif data ==3:
        return 4
    return func(data-1)+func(data-2)+func(data-3)
print(func(6))