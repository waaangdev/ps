t = int(input())
bang = [-1]*1025
bang2 = [-1]*1025
for tt in range(t):
    a,b = map(int,input().split())
    li = []
    sun = -1
    while a:
        li+=[a//b]
        a = a%b
        if(bang[a]==tt):
            sun = bang2[a]
            break
        bang[a]=tt
        bang2[a]=len(li)
        a*=10
        
    print(li[0],end=".")
    if(sun==-1):
        print(''.join(map(str,li[1:]))+"(0)")
    else:
        print(''.join(map(str,li[1:sun]))+"("+''.join(map(str,li[sun:]))+")")
