word_count = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}

C1, C2 = map(int,input().split()) #이름 두개의 각각 길이
N1, N2 = input().split()

R1 , R2 = list(), list()
for i in range(len(N1)):
   R1.append(word_count[N1[i]])

for i in range(len(N2)):
   R2.append(word_count[N2[i]])

#print(R1)
#print(R2)

length = len(R1)+len(R2)
number_list = [*sum(zip(R1,R2),())]

#글자 수가 다를 때? 더 짧은 것이 기준이다.
if len(R1) >= len(R2):
    cut_line = len(R2)
    number_list.extend(R1[cut_line:])
else:
    cut_line = len(R1)
    number_list.extend(R2[cut_line:])

#print(number_list)
#[1, 3, 4, 1, 4, 2, 1, 3, 1, 1, 2, 3, 1, 3, 2, 1]
#나와야 하는 답 1 3 4 1 4 2 1 3 1 1 2 3 1 3 2 1 1 3 3 1 2 3

#result_list = [0 for i in range(length)] #한 번 돌때마다 1씩 감소한 만큼 빈 배열을 만든다.
for count in range(len(number_list)-2):
    #print(number_list)
    for i in range(len(number_list)-1-count):
        number = number_list[i]+number_list[i+1] #1 + 3 = 4
        #print(number)
        if number//10 == 1: #두자리수를 넘어가면 1의 자리만 남기게
            number = number % 10
        number_list[i] = number
result = number_list[0]*10 + number_list[1]
print(str(result)+"%")


        
        