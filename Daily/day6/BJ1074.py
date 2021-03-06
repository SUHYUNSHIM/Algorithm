N,R,C = map(int,input().split()) #사이즈, 행, 열
#z는 0,0을 기준으로 x,y의 숫자

def Z(sz, x ,y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1):
                return (i*2+j) * sz * sz + Z(sz, x-sz*i, y-sz*j)
#(0,0) (0,1) (1,0) (1,1)
# i*2+ j --> 0,1,2,3

print(Z(2**N, R, C))