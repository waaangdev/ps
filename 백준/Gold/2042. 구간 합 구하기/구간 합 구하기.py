"구간 합 구하기"

import sys 
from collections import deque

def tree_cr(locate,rang):
    if(rang[0]+1 == rang[1]):
        li2[locate-1] = li[rang[0]]
        return li[rang[0]]
    li2[locate-1] = tree_cr(locate*2,[rang[0],(rang[0]+rang[1])//2])+tree_cr(locate*2+1,[(rang[0]+rang[1])//2,rang[1]])
    return li2[locate-1]

def tree_add(locate,num,rang):#현재위치,[더할숫자위치,더할숫자]
    
    if(num[0] >= rang[0] and num[0] < rang[1]):
        li2[locate-1] += num[1]
        if(rang[0]+1 != rang[1]):
            tree_add(locate*2,num,[rang[0],(rang[0]+rang[1])//2])
            tree_add(locate*2+1,num,[(rang[0]+rang[1])//2,rang[1]])

def tree_sum(locate,num,rang):#현재위치,[합min,합max]
    #print(locate,num,rang)
    dum = 0
    if(num[0] >= rang[0] and num[0] < rang[1]):
        dum = 1
    elif(num[1] > rang[0] and num[1] <= rang[1]):
        dum = 1
    
    if(num == rang):
        return li2[locate-1]
    elif(rang[0] >= num[0] and rang[1] <= num[1]):
        return li2[locate-1]
    elif(dum):
        return tree_sum(locate*2,num,[rang[0],(rang[0]+rang[1])//2]) + tree_sum(locate*2+1,num,[(rang[0]+rang[1])//2,rang[1]])
    return 0

len_li,dum1,dum2 = map(int,sys.stdin.readline().split()) 
a = dum1+dum2

li = [0 for i in range(len_li)] 
li2 = [0 for i in range(len_li*4)]

for i in range(len_li): 
    li[i] = int(sys.stdin.readline())

tree_cr(1,[0,len_li])

for i in range(a): 
    inp1,inp2,inp3 = map(int,sys.stdin.readline().split())
    if(inp1 == 1):
        tree_add(1,[inp2-1,inp3-li[inp2-1]],[0,len_li])
        li[inp2-1] = inp3
    else:
        print(tree_sum(1,[inp2-1,inp3],[0,len_li]))