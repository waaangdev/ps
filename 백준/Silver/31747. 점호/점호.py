a,b = map(int,input().split())
li = list(map(int,input().split()))
r = 0
p = [0,0]
for i in range(2):
    while p[i] < a:
        if(li[p[i]] == i+1): break
        p[i]+=1
while 1:
    r+=1
    p2 = [0,0]

    if(p[0] == p[1]):break
    #print(p)

    if(abs(p[0]-p[1]) < b):
        p2 = [1,1]
    elif(p[0] < p[1]):
        p2 = [1,0]
    else:
        p2 = [0,1]

    for i in range(2):
        if(p2[i]):
            while p[i] < a:
                p[i]+=1
                if(p[i] < a):
                    if(li[p[i]] == i+1): break

print(r-1)