import sys
from collections import deque

a,inp,bul_g = sys.stdin.readline().split()
a = int(a)
bul_g = int(bul_g)
bul_t = int(inp.split('/')[0])*24*60+int(inp.split('/')[1].split(':')[0])*60+int(inp.split('/')[1].split(':')[1])

month = [0,31,31+28,31*2+28,31*2+28+30,31*3+28+30,31*3+28+30*2,31*4+28+30*2,31*5+28+30*2,31*5+28+30*3,31*6+28+30*3,31*6+28+30*4]
li = {}
li2 = {}
li3 = []


for i in range(a):
    inp = sys.stdin.readline().split()
    t = month[int(inp[0].split('-')[1])-1]*24*60 + int(inp[0].split('-')[2])*24*60 + int(inp[1].split(':')[0])*60 + int(inp[1].split(':')[1])

    bopum = inp[2]
    name = inp[3]
    if(name not in li):
        li[name] = {}
        li2[name] = 0
        li3.append(name)
    if(bopum not in li[name]):
        li[name][bopum] = t
    else:
        li2[name] += max(0,t-li[name][bopum]-bul_t)*bul_g
        del li[name][bopum]


li3.sort()
dum = 0
for i in range(len(li3)):
    if(li2[li3[i]] != 0):
        print(li3[i],li2[li3[i]])
        dum = 1
if(dum == 0):
    print(-1)