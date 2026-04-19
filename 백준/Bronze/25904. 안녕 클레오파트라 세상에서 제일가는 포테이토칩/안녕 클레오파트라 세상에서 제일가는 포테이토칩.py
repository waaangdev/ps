a,c = map(int,input().split())
b = list(map(int,input().split()))
s = -1
while 1:
    for i in range(a):
        if(b[i] >= c):
            c+=1
        else:
            s = i
            break
    if(s != -1):
        break
print(s+1)