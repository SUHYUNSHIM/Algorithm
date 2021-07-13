data_list =[1,2,3,4,5]
data_list2=[[1,2,3],[4,5,6],[7,8,9]]
print(data_list2[0])
print(data_list2[1][1])

m_count =0
for data in range(10):
    for index in range(len(data)):
        if data[index] =='M':
            m_count +=1
print(m_count)