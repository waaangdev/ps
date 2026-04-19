e = int(input())
li = []
a = 0
for i in range(e):
    a+=1
    if(a == 1):
        li.append(0)
        continue
    f = 100000
    v = 100000
    r = li[a-1-1]
    if(a%2 == 0):f = li[a//2-1]
    if(a%3 == 0):v = li[a//3-1]
    if(r <= v and r <= f):
        li.append( r+1)
    elif(f <= v and f <= r):
        li.append( f+1)
    elif(v <= r and v <= f):
        li.append(v+1)
print(li[len(li)-1])