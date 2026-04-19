a = int(input())
def w(q):
    li = []
    
    if(q == 0):
        return ['*','*','*']
    li.append((q*4+1)*'*')
    li.append('*')
    li2 = w(q-1)
    for i in range(len(li2)+1):
        li.append('* ')
        if(i<len(li2)):
            li[2+i] += li2[i]
        else:
            li[2+i] += " "*len(li2[0])
        if(i == 1):
            li[2+i] +=" "*(len(li2[0])-1)
        if(i == 0):
            li[2+i] += "*"
        else:
            li[2+i] += " "
        li[2+i] += "*"
    li.append((q*4+1)*'*')
    return li
if(a == 1):
    print('*')
else:
    qwe = w(a-1)
    for i in range(len(qwe)):
        for j in range(len(qwe[i])):
            print(qwe[i][j],end = '')
        print()