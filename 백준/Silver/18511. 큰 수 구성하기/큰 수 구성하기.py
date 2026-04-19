a,dom = map(int,input().split())
li = list(map(int,input().split()))
li2 = [0 for i in range(10)]
for i in range(dom):
    li2[li[i]] = 1
for i in range(a,-1,-1):
    sti = str(i)
    c = 0
    for j in range(len(sti)):
        if li2[int(sti[j])] == 0:
            c = 1
            break
    if c == 0:
        print(i)
        break
    