


n = int(input())
li = list(map(int,input().split()))
r = 0
way = [[] for i in range(n)]
bang = [True for i in range(n)]
for i in range(n-1):
    inp = list(map(int,input().split()))
    way[i+1].append([inp[0]-1,inp[1]])
    way[inp[0]-1].append([i+1,inp[1]])


def sol(idx,dist,cut):
    global r
    if(dist > li[idx] or cut):
        #print(idx)
        r +=1
        cut=1
    for i in way[idx]:
        if(bang[i[0]]):
            bang[i[0]] = False
            sol(i[0],dist+i[1],cut)
bang[0] = False
sol(0,0,0)
print(r)