a = int(input())
m = []
for i in range(a):
    m.append(list(map(int,input().split())))
ang = [[0,1],[0,-1],[-1,0],[1,0]]
def tzfe(li,mm1):
    mm = [i[:] for i in mm1]
    tt = 1
    for i in range(len(li)):
        tt = 1
        if(li[i] == 0):
            for j in range(a):
                tt = 1
                for k in range(a-2,-1,-1):
                    if(mm[j][k] == 0):
                        tt+=1
                    else:
                        if(mm[j][k+tt] == 0):
                            mm[j][k+tt] = mm[j][k]
                            mm[j][k] = 0
                            tt+=1
                        elif(mm[j][k+tt] == mm[j][k]):
                            mm[j][k+tt] = mm[j][k]*2
                            mm[j][k] = 0
                        else:
                            tt2 = mm[j][k]
                            mm[j][k] = 0
                            mm[j][k+tt-1] = tt2
        if(li[i] == 1):
            for j in range(a):
                tt = 1
                for k in range(1, a,1):
                    if(mm[j][k] == 0):
                        tt+=1
                    else:
                        if(mm[j][k-tt] == 0):
                            mm[j][k-tt] = mm[j][k]
                            mm[j][k] = 0
                            tt+=1
                        elif(mm[j][k-tt] == mm[j][k]):
                            mm[j][k-tt] = mm[j][k]*2
                            mm[j][k] = 0
                        else:
                            tt2 = mm[j][k]
                            mm[j][k] = 0
                            mm[j][k-tt+1] = tt2
        if(li[i] == 2):
            for j in range(a):
                tt = 1
                for k in range(a-2,-1,-1):
    
                    if(mm[k][j] == 0):
                        tt+=1
                    else:
                        if(mm[k+tt][j] == 0):
                            mm[k+tt][j] = mm[k][j]
                            mm[k][j] = 0
                            tt+=1
                        elif(mm[k+tt][j] == mm[k][j]):
                            mm[k+tt][j] = mm[k][j]*2
                            mm[k][j] = 0
                        else:
                            tt2 = mm[k][j]
                            mm[k][j] = 0
                            mm[k+tt-1][j] = tt2
        if(li[i] == 3):
            for j in range(a):
                tt = 1
                for k in range(1, a,1):

                    if(mm[k][j] == 0):
                        tt+=1
                    else:
                        if(mm[k-tt][j] == 0):
                            mm[k-tt][j] = mm[k][j]
                            mm[k][j] = 0
                            tt+=1
                        elif(mm[k-tt][j] == mm[k][j]):
                            mm[k-tt][j] = mm[k][j]*2
                            mm[k][j] = 0
                        else:
                            tt2 = mm[k][j]
                            mm[k][j] = 0
                            mm[k-tt+1][j] = tt2

    r = 0
    for j in range(a):
        for k in range(a):
            r = max(mm[k][j],r)
    
    return r

li = [0 for i in range(5)]
li[4] = -1
end = 0
while 1:
    li[4] += 1   
    for i in range(4,-1,-1):
        if(li[i] == 4 and i != 0):
            li[i-1] += 1
            li[i] = 0
    if(li[0] > 3):
        break  
    end = max(end,tzfe(li,m))    
print(end)
