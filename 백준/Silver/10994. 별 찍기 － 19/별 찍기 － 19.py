e = int(input())
def a(q):
    li = []
    li.append((q*4+1)*'*')
    if(q == 0):
        return li
    qq = a(q-1)
    for i in range(len(qq)+2):
        if(i>0 and i<len(qq)+1):
            li.append('* '+qq[i-1]+' *')
        else:
            li.append('* '+len(qq[0])*' '+' *')
    li.append((q*4+1)*'*')
    return li
qwe = a(e-1)
for i in range(len(qwe)):
    for j in range(len(qwe[i])):
        print(qwe[i][j],end = '')
    print()