import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


li = list(input())
li2 = []
idx = 0
while(idx < len(li)-1):
    if(li[idx][0] in "1234567890" and li[idx+1][0] in "1234567890"):
        li[idx] = li[idx]+li[idx+1]
        del li[idx+1]
    else:
        idx+=1
    #print(li)
for i in range(len(li)):
    if(li[i]=='0'):
        li[i]=''
        li[i-1]=''
    if(li[i] in "-+"):
        pass
    elif(li[i]=='x'):
        li[i]="xx"
    else:
        if(i!=len(li)-1):
            li[i] = str(int(li[i])//2)
        if(li[i]=='1'):li[i]=''
        if(i==len(li)-1):
            li[i]+='x'
r = ''.join(li)
if(r):r+='+'
print(r+'W')
