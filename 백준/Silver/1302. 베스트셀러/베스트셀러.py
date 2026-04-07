maps= {}
maxs = 0
maxi=0
for i in range(int(input())):
    inp=input()
    if(inp in maps):
        maps[inp]+=1
    else:
        maps[inp]=1
    if(maxs < maps[inp] or (maps[inp]==maxs and inp < maxi)):
        maxs=maps[inp]
        maxi=inp
print(maxi)
