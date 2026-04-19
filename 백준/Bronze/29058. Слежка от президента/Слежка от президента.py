import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

# for i in range(int(sys.stdin.readline())):

n,m,k = list(map(int,sys.stdin.readline().split()))
copy = ""
li = ["" for i in range(n)]
page = 0
for i in range(m):
    com=sys.stdin.readline().strip()
    if(com == "Next"):
        page+=1
        page%=n
    elif(com == "Copy"):
        copy = li[page]
        if(len(li[page]) > k):
            copy = li[page][-k:]
    elif(com == "Paste"):
        li[page]+=copy
    elif(com == "Backspace"):
        li[page]= li[page][:-1]
    else:
        li[page]+=com
if(li[page] == ""):
    print("Empty")
else:
    if(len(li[page]) > k):
        print(li[page][-k:])
    else:
        print(li[page])