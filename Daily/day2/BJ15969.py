#가장 높은 점수와 가장 낮은 점수의 차이를 구해라
#행복
num = int(input())
students = list(map(int,input().split()))
#N, lst = input() , list(map(int,input().split()) #한 줄에 받아도 됨.
print(max(students)- min(students))

