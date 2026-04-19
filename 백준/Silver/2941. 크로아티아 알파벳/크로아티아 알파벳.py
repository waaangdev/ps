a = (input())
cro = ['z=','s=','nj','lj','d-','dz=','c-','c=']
q = 0
i = 0
while (i < len(a)):
    for j in range(len(cro)):
        qwe = 0
        if(len(a)-i >= len(cro[j])):
            for k in range(len(cro[j])):
                if(a[i+k] != cro[j][k]):
                    qwe = 1
                    break
            if(qwe == 0):
                q += 1
                i+=len(cro[j])
                break
        else:
            qwe = 1
    if(qwe == 1):
        q += 1
        i+=1
print(q)