N, M = map(int,input().split())
A , B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
AB =''
min_len = min(N,M)
for i in range(min_len):
    AB += A[i] +B[i]

AB += A[min_len:] + B[min_len:]
lst = [alp[ord(i)-ord('A')] for i in AB] #ord() : 특정한 한 문자를 아스키 코드 값으로 변환
#chr() 아스키 코드 값을 문자로 변환.. ord('A') == 65

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
print("{}%".format(lst[0] % 10*10 + lst[1] % 10))
'''
def f(lst):
    ret = []
    for i in range(lst-1):
        ret.append((lst[i]+lst[i+1])%10)
    return ret
'''
