import sys
#from collections import deque
d = int(input())
s = 1
for i in range(d):
    a,b = list(map(int,input().split()))
    if(a == s):
        s = b
    elif(b == s):
        s = a
print(s)