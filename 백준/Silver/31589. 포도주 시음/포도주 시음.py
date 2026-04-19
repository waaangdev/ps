

import sys
n,m = map(int,input().split())
li = list(map(int,sys.stdin.readline().strip().split()))

li.sort()
modes =0
his = 0
r = 0
for i in range(m):
    if(modes == 0):
        r += li[-i//2-1]-his
        #print(li[-i//2-1])
        his = li[-i//2-1]
    elif(modes == 1):
        his = li[i//2]
        #print(li[i//2])
    
    modes = 1-modes
print(r)