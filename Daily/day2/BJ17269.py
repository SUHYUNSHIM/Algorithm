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

#글자 수가 다를 때? 더 짧은 것이 기준이다.
if len(R1) >= len(R2):
    cut_line = len(R2)
else:
    cut_line = len(R1)

for i in range(len(R1)+len(R2)):
    number_list = R1[i] + R2[i]
    if number_list//10 == 1:
        number_list = number_list % 10
