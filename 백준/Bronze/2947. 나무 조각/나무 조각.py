import sys
a = list(map(int,input().split()))
while 1:
    for i in range(4):
        if(a[i] > a[i+1]):
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c
            print(*a)
        if(a == [1,2,3,4,5]):
            break
    if(a == [1,2,3,4,5]):
        break