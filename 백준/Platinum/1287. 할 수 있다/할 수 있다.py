"할 수 있다"
from collections import deque

inp = input()
dp = [0 for i in range(len(inp))]

stack = deque([])
for i in range(len(inp)):
    if(inp[i] == "("):
        stack.append(i)
    elif(inp[i] == ")"):
        if(len(stack) == 0):
            stack.append(i)
            break
        dp[stack.pop()] = i

if(len(stack) != 0):
    
    print("ROCK")

def calc(l,r):
    if(l==r):
        return "ROCK"
    num = ""
    li = deque([])
    i = l
    while(i<r):
        if(inp[i] == "("):
            dum = calc(i+1,dp[i])
            if(dum=="ROCK"): return "ROCK"
            i = dp[i]
            num = dum
        elif(inp[i] in "*+/-"):
            if(num==""):
                return "ROCK"
            li.append(int(num))
            li.append(inp[i] )
            num = ""
        else:
            if(type(num) is int):return "ROCK"
            num += inp[i]

        i+=1
    if(num==""):
        return "ROCK"
    li.append(int(num))
    li2 = deque([])
    lenli = len(li)
    lastnum = "a"
    lastcalc = ""
    #print(li)
    for i in range(lenli):
        popli = li.popleft()

        if(type(popli) is int):
            if(lastcalc != ""):
                if(lastnum == "a"):return "ROCK"

                if(lastcalc == "*"):lastnum = lastnum*popli
                if(lastcalc == "/"):
                    if(popli == 0):return "ROCK"
                    lastnum = lastnum//popli
                lastcalc = ""
            else:
                lastnum = popli
        elif(popli in "*/"):
            if(lastnum == "a"):return "ROCK"
            if(lastcalc != ""):return "ROCK"
            lastcalc = popli
        elif(popli in "+-"):
            li2.append(lastnum)
            li2.append(popli)
            lastnum = "a"
            lastcalc = ""
    if(lastnum == "a"):return "ROCK"
    li2.append(lastnum)
    #print(li2)
            
    r = 0
    lenli2 = len(li2)
    lastnum = "a"
    lastcalc = ""
    for i in range(lenli2):
        popli = li2.popleft()
        if(type(popli) is int):
            if(lastcalc == "-"):
                r -= popli
                lastcalc = ""
                lastnum = popli
            else:
                r += popli
                lastcalc = ""
                lastnum = popli
        elif(popli in "+-"):
            if(lastnum == "a"):return "ROCK"
            lastcalc = popli
            lastnum = "a"
    return r
    
if(len(stack) == 0):
    print(calc(0,len(inp)))