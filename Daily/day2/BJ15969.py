#가장 높은 점수와 가장 낮은 점수의 차이를 구해라
#행복
num = int(input())
students = list(map(int,input().split()))

print(max(students)- min(students))

