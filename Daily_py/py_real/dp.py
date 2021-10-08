#피보나치는 대표적인 동적계획법의 예시이다
#DP 사용x을 경우

def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)

print(fibo(4))
#fibo(3)+fibo(2)
#fibo(3) = fibo(2)+fibo(1)
#fibo(2) = fibo(1)+fibo(0)
#가지에 가지를 내리는 격

#동적 계획법 활용 시
def fibo_dp(num):
    cache = [0 for index in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2,num+1):
        cache[index] = cache[index-1]+cache[index-2]
    return cache[num]
print(fibo(10))
