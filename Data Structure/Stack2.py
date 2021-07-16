data_stack = list() ##=[]
data_stack.append(5)
data_stack.append(2)
data_stack.append(3)
data_stack.append(1)
data_stack.pop()
data_stack.append(1)
data_stack.append(4)
data_stack ## [1,2]
data_stack.pop() ## 2

print(data_stack)
print(data_stack[::-1]) #최상단 원소부터 출력
