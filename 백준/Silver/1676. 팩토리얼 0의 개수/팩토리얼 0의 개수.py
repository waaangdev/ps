from collections import deque
import sys
a = int(input())
s = 1
for i in range(1,a+1):
    s*=i
s = str(s)
ss = 0
for i in range(len(s)-1):
    if(s[len(s)-1-i] == '0'):
        ss+=1
    else:
        break
print(ss)