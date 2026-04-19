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

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
#저기 뭐야 그 중간에서만나기!!!!!!!!!!!!!
#24개들 ㄱㄱ하고 거기서 1쌍더한후 겹치는거있는지
#같은 li2배열이여도1번째수와짝지어진수가다를수있음!!!!!!!!!!!!!!!!!!!!!!!1
#ㄴㅋ

pri = [1 for i in range(2000)]
for i in range(2,2000):
    if(pri[i]):
        for j in range(i+i,2000,i):
            pri[j]=0
#print(pri[:20])

# def m2pow(a,mod):
#     if(a==0):
#         return 1
#     if(a==1):
#         return 2
#     return (m2pow(a//2,mod)**2*(1+a%2))%mod

# pset = [0 for i in range(16777216)]



# rl = []
# li2 = [True for i in range(n)]
# li3 = [0,0]
# def sol(idx,count):
#     #print(idx,li2)
#     if(idx==n):
#         return 1
#     if(not li2[idx]):
#         return sol(idx+1)
    
#     li2[idx]=False
#     li3[idx//25]+=math.pow(2,idx%25)

#     r = 0
#     for i in range(idx+1,n):
#         if(li2[i] and pri[(li[idx]+li[i])]):
#             li2[i] = False
#             li3[i//25]+=math.pow(2,i%25)
#             d = sol(idx+1)
#             r = r or d
#             if(idx==0 and d):
#                 rl.append(li[i])
#             li2[i]=True
#             li3[i//25]-=math.pow(2,i%25)
    

#     li2[idx]=True
#     li3[idx//25]-=math.pow(2,idx%25)

#     if(r):
#         pset.add(tuple(li3))
#     else:
#         impset.add(tuple(li3))

        
#     return r
# sol(0)
# print(len(pset),len(impset))
# if(rl==[]):
#     print(-1)
# else:
#     print(*sorted(rl))





# ways = [[] for i in range(50)]
# bang = [[0 for i in range(50)] for i in range(50)]
# bang2 = [0 for i in range(50)]
# for i in range(n):
#     for j in range(i):
#         if(pri[li[i]+li[j]]):
#             ways[i].append(j)
#             ways[j].append(i)

# print(ways)
# def wayok(qpop,q):
#     r = 0
#     for k in range(2):
#         for i in range(len(ways[qpop[k]])):
#             if(k==0):
#                 nq = [qpop[0],ways[qpop[0]][i]]
#             else:
#                 nq = [ways[qpop[1]][i],qpop[1]]

#             if(nq[1-k]!=qpop[1-k]):
#                 r+=2-bang2[nq[0]]-bang2[nq[1]]
#                 bang2[nq[0]],bang2[nq[1]]=1,1

#                 bang[min(nq)][max(nq)] = 1
#                 q.append(nq)
#                 # if(bang[nq[0]][nq[1]-1000] == mode*2+2):
#                 #     return 0
#     return r

# def bfs(st):
#     q = deque([st])

#     allc = 0
#     bang[min(st)][max(st)] =1
    
#     bang2[st[0]],bang2[st[1]]=1,1

#     allc+=2+wayok(st,q)
#     r = 1
#     while q:
#         #print(q)
#         qpop = q.popleft()
#         for k in range(2):
#             for i in range(len(ways[qpop[k]])):
#                 if(k==0):
#                     nq = [qpop[0],ways[qpop[0]][i]]
#                 else:
#                     nq = [ways[qpop[1]][i],qpop[1]]

#                 if(nq[1-k]!=qpop[1-k]):
#                     if(bang[min(nq)][max(nq)] != 1):

#                         allc+=wayok(nq,q)

#                         allc+=2-bang2[nq[0]]-bang2[nq[1]]
#                         bang2[nq[0]],bang2[nq[1]]=1,1
                        
#                         bang[min(nq)][max(nq)] = 1  
#                         r+=1

#     print(st,r*2,allc)
#     return r*2==allc


# rl = []
# for j in range(len(ways[0])):
#     bang = [[0 for i in range(50)] for i in range(50)]
#     bang2 = [0 for i in range(50)]
#     #if(bang[0][ways[0][j]]==0):#1,2,3,4
#     if(bfs([0,ways[0][j]])):
#         rl+=[li[ways[0][j]]]

#             #print(bang,bfs([i,ways[i][j]],0),bfs([i,ways[i][j]],1))
# if(rl==[]):
#     print(-1)
# else:
#     print(*sorted(rl))

bang = [0 for i in range(50)]
bang2 = [-1 for i in range(50)]
no = -1
def dfs(idx):
    if(bang[idx]):return 0
    bang[idx]=1
    dum = 1
    for i in range(1,n):
        if(i!=no and li[i]%2==1 and pri[li[idx]+li[i]]):

            if(bang2[i]==-1 or dfs(bang2[i])):
                bang2[i] = idx
                return 1
        
    return 0
rl = []
for j in range(1,n):
    if(pri[li[0]+li[j]]):
        no = j
        bang2 = [-1 for i in range(50)]

        rr =0
        for i in range(1,n):
            if(i!=no and li[i]%2==0):
                bang = [0 for i in range(50)]
                rr+=dfs(i)
        if(rr==n//2-1):
            rl+=[li[no]]
        #print(li[no],rr)

if(rl==[]):
    print(-1)
else:
    print(*sorted(rl))
