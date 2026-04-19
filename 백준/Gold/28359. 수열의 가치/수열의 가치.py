import sys

n = int(input())

li = list(map(int,sys.stdin.readline().strip().split()))
li2 = [0]*n

for i in li:
    li2[i-1]+=1
max = 0
maxi = 0
for i in range(n):
    if(li2[i]*(i+1) > max):
        max = li2[i] *(i+1)
        maxi = i+1

li.sort()
#print(li,maxi,max)
rli =[]
p = -1
for i in range(n):
    if(li[i] > maxi):
        if(p == -1):
            p = i
if(p == -1):
    p = n
print(sum(li)+max)
print(*(list(reversed(li[p:]))+li[:p]))