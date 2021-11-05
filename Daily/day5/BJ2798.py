N, M = map(int,input().split())
cards = list(map(int,input().split()))

avg_value = M // 3
cards.sort()
print(cards)
min = 10000000
for i in range(N):
    if abs(avg_value - cards[i]) < min:
        min = avg_value - cards[i]
        index = i
print(index)
result = cards[index]+cards[index-1]+cards[index+1]

print(result)
