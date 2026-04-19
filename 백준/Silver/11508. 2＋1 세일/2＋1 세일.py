"텀프로젝트.미해결"

import sys

a = int(sys.stdin.readline())
li = []
for i in range(a):
    li.append(int(sys.stdin.readline()))
li.sort()
li.reverse()
r = 0
for i in range(a):
    if((i+1)%3 != 0):
        r+=li[i]
print(r)