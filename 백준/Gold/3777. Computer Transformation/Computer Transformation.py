a = 1#1
b = 0#01
c = 0#00
li = []
for i in range(1001):
    li.append(c)
    chis = c
    c=b
    b=a+chis
    a = 2**i
import sys
inp = sys.stdin.readlines()
print('\n'.join([str(li[int(i)]) for i in inp]))