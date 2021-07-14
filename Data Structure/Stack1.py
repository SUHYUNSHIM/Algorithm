##push, pop
##마지막에 넣은 데이터를 가장 먼저 추출하는 방식.
##대표적인 예 재귀 함수.

def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned",data)

recursive(4)