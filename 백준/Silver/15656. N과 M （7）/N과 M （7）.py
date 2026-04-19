import sys
a,b = map(int,input().split())
alpa = sorted(list(map(int,sys.stdin.readline().strip().split())))
#alpa = sorted(input().split())
li = [1 for i in range(b)]
li[b-1] = 0 
while 1:
    c = 0
    li[b-1] += 1   
    for i in range(b-1,-1,-1):
        if(li[i] == a+1 and i != 0):
            li[i-1] += 1
            li[i] = 1
    if(li[0] > a):
        break
    if(c == 0):        
        for i in range(len(li)):
            print(alpa[li[i]-1],end = " ")
        print()