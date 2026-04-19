from collections import deque
import sys


algo = []
pl = {}

a = int(input())
for i in range(a):
    dum = input().split()
    dum[1] = int(dum[1])
    algo.append(dum)

a = int(input())
for i in range(a):
    dum = input().split()
    pl[dum[0]] = int(dum[1])

a = int(input())
name = ""
for i in range(a):
    dum = input().split()
    if(dum[1]=="-"):
        name=dum[0]
        print("hai!")
    else:
        algo.sort(key=lambda x:(abs(x[1]-pl[name]),x[0]))
        print(algo[1][0],"yori mo",algo[0][0])