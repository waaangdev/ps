#체인소 맨
import sys
from collections import deque

n,m,f = (map(int,sys.stdin.readline().strip().split()))
li = [[] for i in range(n)]
for i in range(n): 
    li[i]= sys.stdin.readline().strip()


def xor(a,b):
    return ((a or b) and (not (a and b)))

r = 0

for i in range(n-1):
    dumli = ""
    for j in range(m):
        if(xor(li[i][j] == '.' , li[i+1][j] == '.')):
            dumli+="1"
        elif((li[i][j] == '#' and li[i+1][j] == '#')):
            dumli+="2"
        else:
            dumli+="0"
    dumli = "0"+dumli+"0"
    dumli = dumli.split("2")
    #print(dumli)
    for i in range(len(dumli)):
        if(i == 0 or i ==len(dumli)-1):
            r += min(sum(list(map(int,list(dumli[i])))),f)
        else:
            r += sum(list(map(int,list(dumli[i]))))
    #print(r)

for j in range(m-1):
    dumli = ""
    for i in range(n):
        if(xor(li[i][j] == '.' , li[i][j+1] == '.')):
            dumli+="1"
        elif((li[i][j] == '#' and li[i][j+1] == '#')):
            dumli+="2"
        else:
            dumli+="0"
    dumli = "0"+dumli+"0"
    dumli = dumli.split("2")
    for i in range(len(dumli)):
        if(i == 0 or i ==len(dumli)-1):
            r += min(sum(list(map(int,list(dumli[i])))),f)
        else:
            r += sum(list(map(int,list(dumli[i]))))
    #print(r)
# for i in range(n-1):
#     idx = -1
#     st = 1
#     stlb = -1
#     lb = -1
#     for j in range(m):
#         if(xor(li[i][j] == '.' , li[i+1][j] == '.')):
#             #print("-",j,(li[i][j] == '.' , li[i+1][j] == '.'))
#             if(idx == -1):
#                 idx = j
#             lb = -1
#         elif((li[i][j] == '#' and li[i+1][j] == '#')):
#             if(idx!=-1):
#                 if(st):
#                     #print("asd")
#                     r+=min(j-idx,f)
#                 else:
#                     #r+=j-idx
#                     if(lb != -1):r+=(lb-idx)
#                     else:
#                         #print("asd")
#                         r+=j-idx
#                 # if(st):
#                 #     if(stlb == -1):r+=min(idx-stlb,f)
#                 #     else:r+=min(j-idx,f)
#                 # else:
#                 #     if(lb != -1):r+=min(lb-idx,f)
#                 #     else:r+=min(j-idx,f)
#                 idx = -1
#             st = 0
#         else:
#             if(lb==-1):
#                 lb = j
#             if(st):
#                 stlb = j
#         #print(r)
#     if(idx!=-1):
#         #print(lb,idx,f)
#         if(lb < idx): lb = m
#         r+=min(lb-idx,f)
#         #print("asd")
#     print(r)
#     #print("cuts")
    
# #print("cut")

# for j in range(m-1):
#     idx = -1
#     st = 1
#     stlb = -1
#     lb = -1
#     for i in range(n):
#         if(xor(li[i][j] == '.' , li[i][j+1] == '.')):
#             #print("-",j,(li[i][j] == '.' , li[i+1][j] == '.'))
#             if(idx == -1):
#                 idx = i
#             lb = -1
#         elif((li[i][j] == '#' and li[i][j+1] == '#')):
#             if(idx!=-1):
#                 if(st):
#                     r+=min(i-idx,f)
#                     # if(stlb == -1):r+=min(stlb-idx,f)
#                     # else:r+=min(i-idx,f)
#                 else:
#                     if(lb != -1):r+=(lb-idx)
#                     else:r+=(i-idx)
#                 idx = -1
#             st = 0
#         else:
#             if(lb==-1):
#                 lb = i
#             if(st):
#                 stlb = i
#         #print(r)
#     if(idx!=-1):
#         #print(lb,idx,f)
#         if(lb < idx): lb = n
#         r+=min(lb-idx,f)
#         #print("asd")
#     print(r)
#     #print("cuts")

print(r)