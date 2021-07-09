##두 개의 정수형 변수 입력 받기
a,b = map(int, input().split())

#하나
count = int(input())
##리스트
list1 =[]
list2 = list()
##튜플은 읽기 전용 리스트이다.
tuple1 = tuple()

##입력한 횟수만큼 반복문 수행
count = int(input())
for i in range(count+1):
    if i % 2 ==0:
        continue
    print(i)

#리스트 확장하기
a = [10,20,30]
a.extend([500,600])
a.insert(2,500) ##특정 인덱스에 요소를 추가

a.insert(len(a),500)
a.insert(0,200) ##리스트의 맨 처음에 요소 추가

##인덱스와 요소를 함께 출력하기
a = [38,21,53,62,19]
for index, value in enumerate(a):
    print(index,value )

##while 반복문으로 요소 출력하기
i =0
while i < len(a):
    print(a[i])
    i +=1

##가장 작은 수와 가장 큰 수 구하기
smallest = a[0]
for i in a:
    if i<smallest:
        smallest =i
