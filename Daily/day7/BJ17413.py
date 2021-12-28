word = input()
reverse_name = ''
for c in word:
    reverse_name = c + reverse_name #빈칸 단위, <> 단위로 끊어서 뒤집기를 해야. 그 순서를 유지하도록
print(reverse_name)


