import sys
#map(int,sys.stdin.readline().strip().split())
inp = input()
li = []
dp = [[[0 for i in range(80)] for k in range(80)] for j in range(80)]

def sol(st,ed,prev):
    if(dp[st][ed][prev]):
        return 0
    #print(st,ed,prev)

    if(st==ed):
        if(prev != -1):
            return int(inp[prev:st])<int(inp[ed:])
        else:
            return 1
    
    for i in range(ed-st):
        if(prev != -1 and int(inp[st:ed-i]) <= int(inp[prev:st])):continue
        if(sol(ed-i, ed,st)): 
            li.insert(0,inp[st:ed-i])
            return 1
        
    dp[st][ed][prev]=1
    return 0

for i in range(len(inp)):
    if(sol(0,len(inp)-i-1,-1)):
        print(int(inp[len(inp)-i-1:]))
        break