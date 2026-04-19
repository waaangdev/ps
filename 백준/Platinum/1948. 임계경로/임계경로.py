from sys import *
setrecursionlimit(10001)
input=stdin.readline
z=print
f=int
n=f(input())
m=f(input())
t=[0]*n*3
w=[[]for i in t]
def o():return map(f,input().split())
for i in' '*m:
 p,u,c=o()
 w[p]+=[(u,c)]
 w[u+n]+=[(p+n,c)]
p,q=o()
def s(x):
 if not t[x]:
  for i,j in w[x]:t[x]=max(t[x],s(i)+j)
 return t[x]
s(p)
s(q+n)
r,e=0,0
for i in range(n):
 for j,k in w[i]:
  d=t[i+n]+t[j]+k;e=(r<=d)+e*(r>=d);r=max(r,d)
z(r)
z(e)