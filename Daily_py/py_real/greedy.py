#동전 개수 최소 지불 문제
#그 단계에서 최적의 조합 = 솔루션을 찾는 것이기 때문이다.
#지불해야 하는 값이 4720원일 때, 1원, 50원, 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오
def coin_pay(value,coin_list):
    total_coin = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin,details
data_list = [1,100,50,500]

#print(coin_pay(4720,data_list))

#가방 냅색 문제 - 무게 제한에 맞춰, 최대 가치를 가지도록 물건을 넣어라.
#쪼갤 수 있다.
#쪼갠 다면 비율을 이용한다.  10달러에 20개이다. 근데 남은 돈은 5달러이다.그러면 10개를 산다.
# 비용 분에 가치  -> 20/10 이것이 큰 순서대로 처리한다. # 비용 5달러 분에 10달러 는 1/2. 이 비율을 가치에 곱한다.
data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list,key = lambda x:x[1]/x[0],reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0],data[1],1]) #하나의 리스트 요소로 담기게
            #1의 의미는 100% 반영되었다는 것이다.
        else:
            fraction = capacity / data[0] #나눗셈 결과 float . 5/2 = 2.5 . 몇 퍼센트가 반영되었는지
            total_value += data[1] * fraction
            details.append([data[0],data[1],fraction])
            break #더 이상 할 수 없는 정도이기 때문에
    return total_value , details

print(get_max_value(data_list,30))
