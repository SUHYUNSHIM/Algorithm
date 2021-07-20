array1 =[i for i in range(20) if i%2 == 1]
array2 = [i*i for i in range(1,10)]

#[[0,0,0,0],[0,0,0,0],[0,0,0,0]] -->2차원 리스트를 활용해 인접 행렬을 표현할 수 있다.
n=3
m=4
array3 =[[0]*m for _ in range(n)]

#포함되어 있지 않은 원소만 넣는다
a =  [1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]

#dict
data = dict()
data['사과'] ='Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
## ['사과':'Apple', '바나나':'Banana', '코코넛:' Coconut']

#집합 자료형
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
#합집합 a|b , a&b , a-b
a.add(6)
a.update([5,6])
a.remove(3)


