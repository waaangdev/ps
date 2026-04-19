import math
a,b = map(int,input().split())
li = [0 for i in range(a,b+1)]
for i in range(int(math.sqrt(b))):
    for j in range(len(li)):
        if(li[j] == 0):
            if((a+j) % (i+2) == 0 and (a+j) != (i+2)):
                li[j] = 1
for j in range(len(li)):
    if(li[j] == 0 and a+j != 1):
        print(a+j)