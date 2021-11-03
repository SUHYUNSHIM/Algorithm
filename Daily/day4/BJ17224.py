N,L,K = map(int,input().split()) #문제 개수, 역량, 최대 풀 수 있는 문제 개수
easy_one, hard_one = list(),list()
score = 0
cnt = 0
for i in range(N): #hard, easy 나눠서 리스트에 각각 넣기
    easy, hard = map(int, input().split())
    easy_one.append(easy)
    hard_one.append(hard)

hard_cut = 0
for i in range(N):
    if hard_one[i] <= L:
        if K == 0:
            break
        score += 140
        K-= 1
        hard_cut +=1
#print("중간 집계"+str(score))
#print("남은 K는 "+str(K))
#print("푼 문제번호는 "+str(hard_cut)+"까지 이다")
if K >0:
    for i in range(hard_cut,N):
        if easy_one[i] <= L:
            if K == 0:
                break
            score += 100
            K -= 1
print(score)
    