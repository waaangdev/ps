import math
import sys
n,m=list(map(int,sys.stdin.readline().split()))
print(math.factorial(n)//math.factorial(n-m)//math.factorial(m))