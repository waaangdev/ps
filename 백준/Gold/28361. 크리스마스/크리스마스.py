import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
print(n)
if(((n%3==2)*1)):
    sys.stdout.write(str(1)+" ")
idx = 1+((n%3==2)*1)
for i in range(n//3):
    sys.stdout.write(str(idx)+" ")
    sys.stdout.write(str(idx+2)+" ")
    sys.stdout.write(str(idx+1)+" ")
    idx += 3
if(n%3==0):
    sys.stdout.write(" "+str(1)+"") 
elif(n%3==1):
    sys.stdout.write(str(n)+"")
    sys.stdout.write(" "+str(1)+"") 
else:

    sys.stdout.write(str(n)+"")
    sys.stdout.write(" "+str(1)+"") 