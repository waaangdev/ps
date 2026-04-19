a = int(input())
ma = 0
ma1 = 0
li = []
for i in range(a):
    b = int(input())
    if(b >= ma):
        ma = b
        ma1 = i
    li.append(b)
t = 0
while 1:
    if(ma1 == 0):
        break
    li[ma1] -=1
    li[0] +=1
    
    ma = 0
    ma1 = 0
    for i in range(a):
        if(li[i] >= ma):
            ma = li[i]
            ma1 = i
    t+=1
print(t)