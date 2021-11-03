N = int(input())
S = input()

bonus = 0
sum = 0

for index in range(N):
    if S[index] == 'X':
        bonus = 0
        #print(str(index+1)+"번째")
        #print(bonus)
    elif S[index] == 'O':
        sum += index+1
        sum += bonus
        #print(str(index+1)+"번째")
        #print(sum)
        bonus += 1
print(sum)

'''
N, S = input(), input()
score, bonus = 0,0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx+1+bonus # score, bonus = score + idx +1 +bonus , bonus+1
        bonus +=1
    else:
        bonus =0
print(score)
'''
