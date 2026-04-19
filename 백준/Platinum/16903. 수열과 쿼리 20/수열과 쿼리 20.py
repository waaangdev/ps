import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li1 = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)
import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li1 = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)
seg = [[],[],[0,0]]
for i in range(int(sys.stdin.readline())):
    m,x = list(map(int,sys.stdin.readline().split()))
    x2 = x
    x = bin(x)[2:]
    x=(31-len(x))*'0'+x
    if(m!=3):
        segi = seg
        for j in x:
            segi[2][int(j)]+= 3-m*2
            if(segi[int(j)]==[]):
                segi[int(j)]=[[],[],[0,0]]
            segi=segi[int(j)]
        
    else:
        #print(seg)
        segi = seg
        r = ""
        for j in x:
            dl = [1,0]
            if(j=='1'): dl=[0,1]
            d = '1'
            for k in dl:
                if(segi[2][k]!=0):
                    r+=d
                    segi=segi[k]
                    break
                d = '0'
        #print(x,r)
        if(r==''):
            print(x2)
        else:
            r = int("0b"+r,base=2)
            print(max(x2,r))

# seg = [[],[],[0,0]]
# all = "0"*31
# for i in range(int(sys.stdin.readline())):
#     m,x = list(map(int,sys.stdin.readline().split()))
#     x2 = x
#     x = bin(x)[2:]
#     x=(31-len(x))*'0'+x
#     if(m!=3):
#         r = ""
#         for j in range(31):
#             if(all[j]!=x[j]):
#                 r+="1"
#             else:
#                 r+='0'
#         x = r
        
#         segi = seg
#         for j in x:
#             segi[2][int(j)]+= 3-m*2
#             if(segi[int(j)]==[]):
#                 segi[int(j)]=[[],[],[0,0]]
#             segi=segi[int(j)]
        
#     else:
#         #print(seg)
#         segi = seg
#         r = ""
#         for j in range(31):
#             if(all[j]!=x[j]):
#                 r+="1"
#             else:
#                 r+='0'
#         all = r

#         r = ""
#         for j in all:
#             dl = [1,0]
#             if(j=='1'): dl=[0,1]
#             d = '1'
#             for k in dl:
#                 if(segi[2][k]!=0):
#                     r+=d
#                     segi=segi[k]
#                     break
#                 d = '0'
#         #print(all,r)
#         r = int("0b"+r,base=2)
#         print(r)

# li=[]
# for i in range(int(sys.stdin.readline())):
#     m,x = list(map(int,sys.stdin.readline().split()))
#     if(m==1):
#         li.append(x)
#     elif(m==2):
#         li.remove(x)
#     else:
#         for i in range(len(li)):
#             li[i] = li[i]^x
#         print(max(li))