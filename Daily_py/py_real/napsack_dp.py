'''
백준 12865
https://gsmesie692.tistory.com/113
https://chanhuiseok.github.io/posts/improve-6/
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이다.
출력 한 줄에 배낭을 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

입력 예시
4 7
6 13
4 8
3 6
5 12

출력 14
'''
import sys
wt = []
val=[]
N,K = map(int,sys.stdin.readline().strip().split()) #입력은 문자열, 정수로 변환

def knapsack(W,wt,val,n): #W는 배낭의 무게한도, wt는 각 보석의 무게, val는 각 보석의 가격, n은 보석의 수
        K = [[0 for x in range(W+1)] for x in range(n+1)] #DP를 위한 2차원 리스트
        #print(K)
        for i in range(n+1):
            for w in range(W+1): #각 칸을 돌면서
                if i==0 or w==0: #0번째 행,열은 0으로 세팅
                    K[i][w] =0
                elif wt[i-1] <=w and w-wt[i-1]>=0: #점화식
                    K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w]) #max 함수 사용하여 큰 것 선택
                else:
                    K[i][w] = K[i-1][w]
        return K[n][W]

for i in range(N):
    w,v = map(int,sys.stdin.readline().strip().split())
    wt.append(w)
    val.append(v)
print(knapsack(K,wt,val,N))
