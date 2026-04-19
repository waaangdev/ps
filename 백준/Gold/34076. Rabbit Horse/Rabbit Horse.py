
import sys


def c(n):
    return n*(n-1)//2

a = int(input())
if(a<11):
    print("a"*a)
else:
    li = [1]*10
    li[2] = 2

    r = 1
    for _ in range(a-11):
        maxr = 0
        maxri = 0
        for i in range(10):
            dum = 0
            if(i!=2):
                dum = r//(li[i])*(li[i]+1)
            else:
                dum = r//c(li[i])*c(li[i]+1)
            if(dum > maxr):
                maxr = dum
                maxri = i

        li[maxri]+=1
        r= maxr

    for i in range(10):
        print("RabitHorse"[i]*li[i],end='')
