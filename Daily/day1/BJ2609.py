import math
a,b = map(int, input().split())
'''
시간초과
#최대 공약수
for i in range(min(a,b),0,-1):
    if (a % i == 0) and (b % i == 0):
        print(i)
        break
#최소 공배수
for i in range(max(a,b),(a*b)+1):
    if (i % a == 0) and (i % b == 0):
        print(i)
        break
'''
minCommon = math.gcd(a,b)
maxCommon = a * (b/minCommon)
print (minCommon)
print (int(maxCommon))

#유클리드 호제법 + 0730
'''
2개의 자연수를 받아 최대공약수를 받기 위해 2부터
두 자연수 중 작은 자연수까지 모두 나누어보면서 가장 큰 공약수를 구할 수 있다.

정의
2개의 자연수 a,b에 대하여 a가 b보다 클 때, a를 b로 나눈 나머지를 r이라 하면, a와 b의 
최대 공약수는 b와 r의 최대공약수와 같다. 이 성질을 따라 b를 r로 나눈 나머지 r2를 구하고,
다시 r을 r2로 나눈 나머지를 구하는 과정을 재귀를 타고 들어가다 나머지가 0이 되면 그 나누는 수가 a와 b의 
최대공약수이다. 

GCD(A,B) = GCD(B, A%B)
if A % B == 0 -> GCD = B
else GCD(B,A%B)

최소 공배수는 -> 최대 공약수를 이용해서 푼다.
'''
'''
a,b = map(int, input().split())
def gcd(a,b):
     if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

if a>b:
    gcd = gcd(a,b)
    lcm = (a*b)
    print(gcd)
    print(lcm)
else:
    gcd = gcd(b,a)
    lcm = (a*b)
    print(gcd)
    print(lcm)

'''

