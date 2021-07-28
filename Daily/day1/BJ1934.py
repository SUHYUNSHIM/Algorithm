import math
T = int(input())
value = []*T

for _ in range(T):
    A, B = map(int,input().split())
    minCommon = math.gcd(A, B)
    maxCommon = A * (B / minCommon)
    value.append(int(maxCommon))

for a in value:
    print(a)