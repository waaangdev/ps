a,b = map(int,input().split())
li = [1 for i in range(b)]
li[b-1] = 0 
while 1:
    c = 0
    li[b-1] += 1   
    for i in range(b-1,0,-1):
        if(li[i] == a+1):
            li[i-1] += 1
            li[i] = 1
    for i in range(b-1): 
        if(li[i] > li[i+1]):
            c = 1
            break
    if(li[0] > a):
        break
    if(c == 0):
        print(*li)