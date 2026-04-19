a = int(input())
li = {}
li2 = []
for i in range(a):
    b = input().split()
    li[b[0]] = i
    li2.append([b[1],b[2]])
def jun(qwe):
    if(li2[li[qwe]][0] == '.' and li2[li[qwe]][1] == '.'):
        return qwe
    elif(li2[li[qwe]][0] == '.'):
        return qwe+jun(li2[li[qwe]][1])
    elif(li2[li[qwe]][1] == '.'):
        return qwe+jun(li2[li[qwe]][0])
    return qwe+jun(li2[li[qwe]][0])+jun(li2[li[qwe]][1])

def jung(qwe):
    if(li2[li[qwe]][0] == '.' and li2[li[qwe]][1] == '.'):
        return qwe
    elif(li2[li[qwe]][0] == '.'):
        return qwe+jung(li2[li[qwe]][1])
    elif(li2[li[qwe]][1] == '.'):
        return jung(li2[li[qwe]][0])+qwe
    return jung(li2[li[qwe]][0])+qwe+jung(li2[li[qwe]][1])
def hu(qwe):
    if(li2[li[qwe]][0] == '.' and li2[li[qwe]][1] == '.'):
        return qwe
    elif(li2[li[qwe]][0] == '.'):
        return hu(li2[li[qwe]][1])+qwe
    elif(li2[li[qwe]][1] == '.'):
        return hu(li2[li[qwe]][0])+qwe
    return hu(li2[li[qwe]][0])+hu(li2[li[qwe]][1])+qwe

print(jun("A"))
print(jung("A"))
print(hu("A"))