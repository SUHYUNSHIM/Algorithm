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
