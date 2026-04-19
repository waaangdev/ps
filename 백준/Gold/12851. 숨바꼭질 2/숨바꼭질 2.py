a1,b1  = map(int,input().split())
br = 0
lili = 0
lll = [[0 for i in range(100001)],[0 for i in range(100001)]]
t = 0
mm = [a1]
if(a1 == b1):
    t = 0
    lili = 1
elif(a1 > b1):
    t = a1-b1
    lili = 1
else:
    lll[1][a1] = 1
    while 1:
        t += 1
        mm1 = len(mm)
        aaa = 0
        for i in range(mm1):
            if(lll[t%2][mm[0]] != 0):
                aaa +=1
                mm2 = mm[0]
                qweqweqwe = lll[t%2][mm2]
                c = mm2*2
                d = mm2+1
                e = mm2-1
                if(c < 100001 and c >= 0):
                    if(lll[(t%2)*-1+1][c] == 0):mm.append(c)
                    lll[(t%2)*-1+1][c] += qweqweqwe
                if(d < 100001 and d >= 0):
                    if(lll[(t%2)*-1+1][d] == 0):mm.append(d)
                    lll[(t%2)*-1+1][d] += qweqweqwe
                if(e < 100001 and e >= 0):
                    if(lll[(t%2)*-1+1][e] == 0):mm.append(e)
                    lll[(t%2)*-1+1][e] += qweqweqwe
                if(c == b1):
                    lili+=lll[(t%2)*-1+1][c]
                    lll[(t%2)*-1+1][c] = 0
                    br = 1
                if(d == b1):
                    lili+=lll[(t%2)*-1+1][d]
                    lll[(t%2)*-1+1][d] = 0
                    br = 1
                if(e == b1):
                    lili+=lll[(t%2)*-1+1][e]
                    lll[(t%2)*-1+1][e] = 0
                    br = 1
            del mm[0]
        if(br == 1):
            break

print(t)
print(lili)