word = input().split()

temp_name = ''
cnt = 0

#aprint(word)
for c in word:
    reverse_name = ''
    for d in range(len(c)):
        a = True
        if c[d] == '<':

            temp_name = temp_name + reverse_name
            temp_name = temp_name + c[d]
            d = d + 1
            while a:
                temp_name = temp_name + c[d]
                d = d + 1
                if c[d] == '>':
                    temp_name = temp_name + c[d]
                    a = False
                    cnt = cnt + 1

        reverse_name = c[d] + reverse_name + ''  # 빈칸 단위, <> 단위로 끊어서 뒤집기를 해야. 그 순서를 유지하도록
    if cnt == 0:
        temp_name = temp_name + reverse_name + ' '

print(temp_name)
#baekjoon online judge
#<open>tag<close>



