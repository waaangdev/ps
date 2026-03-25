import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

n,k=list(map(int,sys.stdin.readline().split()))
li = [0]*n
def f(x):
    l,r = 1,n
    while(l<=r):
        mid = (l+r)//2
        if(li[mid-1]==x):return 1
        elif(li[mid-1]<x): l=mid+1
        elif(li[mid-1]>x): r=mid-1
    return 0

for i in range(n):
    li[i]=n-i

def sol(l,r,k,num,num2):
    if(l>r):
        return 
    
    
    mid = (l+r)//2
    li[mid-1]=[num,mid-1]
    if(k>=(r-l+1)-1):
        sol(l,mid-1,0,num+num2,num2//2)
        sol(mid+1,r,0,num-num2,num2//2)
    elif(k==((mid-1)-l+1)):
        sol(l,mid-1,0,num+num2,num2//2)
        sol(mid+1,r,0,num+num2,num2//2)
    elif(k>=(r-(mid+1)+1)):
        sol(l,mid-1,k-(r-(mid+1)+1),num-num2,num2//2)
        sol(mid+1,r,0,num-num2,num2//2)
    else:
        sol(l,mid-1,k,num-num2,num2//2)
        sol(mid+1,r,0,num+num2,num2//2)

sol(1,n,n-k,0,2097152)
li.sort()
for i in range(n):
    li[i][0]=i+1
li2 = [0]*n
for i in range(n):
    li2[li[i][1]]=li[i][0]
if(k!=0):
    print("YES")
    print(*li2)
else:
    print("NO")
c=0
# for i in range(n):
#     c+=f(li[i])
#print(c)