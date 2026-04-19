import sys
from collections import deque

a,b = map(int,input().split())

mul_m = [0b0 for _ in range(a)]
mul_q = deque([])
dol_m = [0b0 for _ in range(a)]
go_st = []
go_m = [0b0 for _ in range(a)]
end = []

ang = [[0,1],[-1,0],[0,-1],[1,0]]

for i in range(a):
    inp = sys.stdin.readline().strip()
    
    for j in range(b):
        if(inp[j] == '*'):
            mul_m[i] |= (1<<j)
            mul_q.append([i,j])
        if(inp[j] == 'X'):dol_m[i] |= (1<<j)
        if(inp[j] == 'D'):end = [i,j]
        if(inp[j] == 'S'):
            go_m[i] |= (1<<j)
            go_st = [i,j]
        
go_q = deque([go_st[:]])

r = 0
br = 0

while 1:
    r += 1
    lengoq = len(go_q)
    if(lengoq == 0):
        r = -1
        break
    for i in range(lengoq):
        goqpop = go_q.popleft()
        if(mul_m[goqpop[0]] & (1<<goqpop[1]) != 0):
            continue
        for j in range(4):
            if(goqpop[0]+ang[j][0] < a and goqpop[0]+ang[j][0] >= 0 and goqpop[1]+ang[j][1] < b and goqpop[1]+ang[j][1] >= 0):
                if(go_m[goqpop[0]+ang[j][0]] & (1<<goqpop[1]+ang[j][1]) == 0):
                    if(dol_m[goqpop[0]+ang[j][0]] & (1<<goqpop[1]+ang[j][1]) == 0):
                        if(mul_m[goqpop[0]+ang[j][0]] & (1<<goqpop[1]+ang[j][1]) == 0):
                            
                            go_m[goqpop[0]+ang[j][0]] |= (1<<goqpop[1]+ang[j][1])
                            
                            go_q.append([goqpop[0]+ang[j][0],goqpop[1]+ang[j][1]])
                            if([goqpop[0]+ang[j][0],goqpop[1]+ang[j][1]] == end):
                                br = 1
                                break
        if(br == 1):break
    if(br == 1):break
    
    
    for i in range(len(mul_q)):
        goqpop = mul_q.popleft()
        for j in range(4):
            if(goqpop[0]+ang[j][0] < a and goqpop[0]+ang[j][0] >= 0 and goqpop[1]+ang[j][1] < b and goqpop[1]+ang[j][1] >= 0):
                if(mul_m[goqpop[0]+ang[j][0]] & (1<<goqpop[1]+ang[j][1]) == 0):
                    if(dol_m[goqpop[0]+ang[j][0]] & (1<<goqpop[1]+ang[j][1]) == 0):
                        if([goqpop[0]+ang[j][0],goqpop[1]+ang[j][1]] != end):
                            
                            mul_m[goqpop[0]+ang[j][0]] |= (1<<goqpop[1]+ang[j][1])
                            
                            mul_q.append([goqpop[0]+ang[j][0],goqpop[1]+ang[j][1]])
                            
                            
                        
if(r == -1):
    print("KAKTUS") 
else:               
    print(r)