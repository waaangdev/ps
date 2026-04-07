sets = set()
for i in range(int(input())):
    inp=input().split()
    if(inp[1]=='enter'):
        sets.add(inp[0])
    else:
        sets.remove(inp[0])
sets = sorted(list(sets))[::-1]
print('\n'.join(sets))