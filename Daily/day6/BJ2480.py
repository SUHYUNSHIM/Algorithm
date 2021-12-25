a, b, c = map(int,input().split())

#주사위 3개
def rewards(d1,d2,d3):
    reward = 0
    dlist = []
    clist = []
    dlist.append(d1)
    dlist.append(d2)
    dlist.append(d3)
    if d1 == d2 == d3:
        reward += 10000 + d1 * 1000
        return reward
    else:
        for i in dlist:
            clist.append(dlist.count(i))
        for j in range(len(clist)):
            if clist[j] == 2:
                reward = 1000 + dlist[j] * 100
                return reward
            elif max(clist) == 1:
                #print(dlist)
                reward = max(dlist) * 100
                return reward
print(rewards(a,b,c))



