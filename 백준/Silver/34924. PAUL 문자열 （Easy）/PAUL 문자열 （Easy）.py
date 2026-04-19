import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = sys.stdin.readline().strip()
c = 0
r = "YES"
r2 = ""
for i in range(n):
    if(li[i] in "PAUL"):
        if(c%2 !=0):
            r = "NO"
        r2+=li[i]
        c = 0
    else:
        c+=1
if(c%2 !=0 or r2 != "PAUL"):
    r = "NO"
print(r)