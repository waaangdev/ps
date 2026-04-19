import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li2 = [0 for i in range(n)]
var = [n for i in range(n*2+1)]
vari = 0
for i in range(1,n):
    if(li[i] != li[i-1]):
        var[vari] = i
        vari+=1
    li2[i] = vari
#print(li)
#print(li2,var)
r = 0
for i in range(n):
    if(li[i] == 0):
        dum = var[li2[i]]
        r+=(var[li2[i]]-i)*1
        r+=(n-var[li2[i]])*2
    elif(li[i] == 1):
        dum = var[li2[i]]
        r+=(var[li2[i]]-i)*0
        r+=(n-var[li2[i]])*2
        
print(r)