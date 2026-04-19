a,b = map(int,input().split())
st = input()
li = [0]*a
for i in range(a):
    if(st[i] == 'P'):
        for j in range(-b,b+1):
            if(j!=0):
                if(i+j >= 0 and i+j < a):
                    if(st[i+j] == 'H'):
                        if(li[i+j]==0):
                            li[i+j]=1
                            break
print(sum(li))