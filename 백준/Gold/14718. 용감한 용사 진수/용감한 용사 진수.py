a,b = map(int,input().split())
li = []
for i in range(a):
    li.append(list(map(int,input().split())))
r = -1
for i in range(a):
    for j in range(a):
        for k in range(a):
            q,w,e = li[i][0],li[j][1],li[k][2]
            dum = 0
            for l in range(a):
                if(li[l][0] <= q and li[l][1] <= w and li[l][2] <= e):
                    dum +=1
            if(dum >= b):
                r = min(q+w+e,r)
                if(r == -1):
                    r = q+w+e
print(r)

