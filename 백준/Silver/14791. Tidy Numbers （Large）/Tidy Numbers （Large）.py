inp = []

def sol(inp,lnum):
    if(inp == []):
        return []
    dum = sol(inp[1:],inp[0])
    if(dum != [-1]):
        if(inp[0] < lnum):
            return [-1]
        return [inp[0]]+dum
    else:
        inp[0]-=1
        if(inp[0] < lnum):
            return [-1]
        else:
            return [inp[0]]+[9]*(len(inp[1:]))


for i in range(int(input())):
    inp = list(map(int,list(input())))
    r =sol(inp,0)
    while(r[0]==0):
        del r[0]
    print(f"Case #{i+1}: {''.join(map(str,r))}")