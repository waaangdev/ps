
a1,b1  = map(int,input().split())
li = [[a1,0]]
br = 0
mean2 = -1
lll = [0 for i in range(150001)]
lll1 = [0 for i in range(150001)]
t = 1000000
tt = 0
if(a1 == b1):
    t = 0
elif(a1 > b1):
    t = a1-b1
else:
    while 1:
        le = len(li)
        for i in range(le):
            c = [li[0][0]*2,li[0][1]+1]
            d = [li[0][0]+1,li[0][1]+1]
            e = [li[0][0]-1,li[0][1]+1]
            if(c[0] == b1):
                t = min(t,c[1])
            if(d[0] == b1):
                t = min(t,d[1])
            if(e[0] == b1):
                t = min(t,e[1])
            if(c[0] >= 0 and c[0] < len(lll)-1):
                if(lll[c[0]] == 0 or lll1[c[0]] > c[1]):
                    li.append(c)
                    lll[c[0]] = 1
                    lll1[c[0]] = c[1]
                    tt+=1
            if(d[0] >= 0 and d[0] < len(lll)-1):
                if(lll[d[0]] == 0 or lll1[d[0]] > d[1]):
                    li.append(d)
                    lll[d[0]] = 1
                    lll1[d[0]] = d[1]
                    tt+=1
            if(e[0] >= 0 and e[0] < len(lll)-1):
                if(lll[e[0]] == 0 or lll1[e[0]] > e[1]):
                    li.append(e)
                    lll[e[0]] = 1   
                    lll1[e[0]] = e[1]
                    tt+=1
            del li[0]
     
        if(tt >= len(lll)-1):
            break
print(t)