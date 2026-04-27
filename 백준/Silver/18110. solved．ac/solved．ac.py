import sys
import math

n = int(input())
li=[int(sys.stdin.readline()) for i in range(n)]
n2 = round(n*3/20+0.00001)

li.sort()
if(n==0):
    print(0)
else:
    #print(li[n2:-n2],n2)
    print(round(sum(li[n2:n-n2])/(n-n2*2)+0.00001))