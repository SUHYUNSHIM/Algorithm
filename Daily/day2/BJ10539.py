#수빈이와 수열
length = int(input())
nums = list(map(int,input().split()))
original = list()

for index in range(len(nums)):
    if index == 0:
        original.append(nums[index])  # 초기값 설정
    else:
        result = nums[index] * (index+1) - sum(original[:index])
        #original[index] = result #직접 인덱스를 설정하여 대입하는 것은 인덱스 범위 오류가 난다.
        original.append(result)

for result in original:
    print(result, end=' ')

'''
N,B = int(input()), list(map(int,input().split()))
A= [B[0]]

for i in range(1,N):
    A.append(B[i]*(i+1) - sum(A))


# A = [0 for i in range(B)]
#A[0] = B[0]
#for i in range(1,N):
#    A[i] = (B[i]*(i+1) -sum(A))

for i in A:
    print(i, end=' ')
'''
