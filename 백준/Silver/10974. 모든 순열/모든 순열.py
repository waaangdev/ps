a =int(input())
def qwe(n):
    if(n == 1):
        return ["1"]
    li = qwe(n-1)
    r = []
    for i in range(n,0,-1):
        if(i!=n):
            for j in range(len(li)):
                li[j] = li[j].replace(str(i), str(i + 1))
        li2= li[:]
        for j in range(len(li)):
            li2[j]=str(i)+" "+li2[j]
        r = li2[:]+r

    return r
li = qwe(a)
for j in li:
    print(j)