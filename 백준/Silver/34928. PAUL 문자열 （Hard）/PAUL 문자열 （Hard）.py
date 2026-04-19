import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = sys.stdin.readline().strip()
r=0
for i in range(n):
    if(li[i] == "P" and r == 0):
        if(i%2 == 0):
            r+=1
    
    if(li[i] == "A" and r == 1):
        if(i%2 == 1):
            r+=1
            
    if(li[i] == "U" and r == 2):
        if(i%2 == 0):
            r+=1
            
    if(li[i] == "L" and r == 3):
        if(i%2 == 1):
            r+=1
if(r==4 and n%2 == 0):
    print("YES")
else:
    print("NO")