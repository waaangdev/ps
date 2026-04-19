
a1,b1  = map(int,input().split())
li = [a1]
t = 0
br = 0
mean2 = -1
while 1:
    t+=1
    le = len(li)
    for i in range(le):
        c = li[0]*2
        d = int(str(li[0])+"1")
        if(c == b1 or d == b1):
            br = 1 
            break
        if(c < b1):
            li.append(c)
        if(d < b1):
            li.append(d)
        del li[0]
 
    if(len(li) == 0):
        t =-2
        break
    if(br == 1):
        break
print(t+1)