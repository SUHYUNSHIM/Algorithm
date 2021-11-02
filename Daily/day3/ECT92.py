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











