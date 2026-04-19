a = int(input())
al = list(map(int,input().split()))
li1 = []
d = 0
d1 = 0 # 숫자를 삽입할 위치
for i in range(a):
    d =al[i]
    
    if(len(li1) == 0):
        d1 = 0
    else:
        #이분탐색
        sort1 = -1
        sort2 = len(li1)
        while 1:
            if(li1[(sort1+sort2)//2] > d):
                sort1 = (sort1+sort2)//2
            elif(li1[(sort1+sort2)//2] < d):
                sort2 = (sort1+sort2)//2
            else:
                d1 = (sort1+sort2)//2+1
                break
            if(abs(sort1 - sort2) < 2):
                d1 = (sort1+sort2)//2+1
                break
        #이분탐색
    #print(d1)
    
    if(len(li1) == 0):
        li1.append(d)
    elif(len(li1)-1 < d1):
        if(d != li1[len(li1)-1]):
            li1.append(d)
    else:
        if(li1[d1] < d):
            if(d1 == 0):
                li1[d1] = d
            
            elif(d != li1[d1-1]):
                li1[d1] = d
    #input(li1)
print(len(li1))