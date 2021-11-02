N,M,K = map(int,input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
sum = 0
cnt = M
while cnt > 0:
    if numbers[1] == numbers[0]:
        sum += numbers[0]* M
        cnt = 0
    else:
        sum += numbers[0] * K
        cnt -= K
        sum += numbers[1]
        cnt -= 1
        if cnt == 0:
            break
        elif cnt >= K+1:
            sum += (cnt // (K+1)) * (numbers[0]*K + numbers[1])
            sum += (cnt % (K+1)) * numbers[0]
            cnt = 0
print(sum)

'''
result = 0
first = numbers[0]
second = numbers[1]
while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -=1 #반복문을 도는 동안 최댓값이 더해지고, 합을 완성할 수 있는 count의 수를 감소시킨다. 
    if M == 0:
        break
    result += second
    M -=1
print(result)
'''

'''
count = int((m/k+1)) * K
count += m %(k+1)

result = 0
result += (count) * first
result += (m-count) * second

'''











