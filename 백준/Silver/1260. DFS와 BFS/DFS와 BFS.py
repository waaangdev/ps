a,b,c = map(int,input().split())
li2 = []
li22 = []
for i in range(b):
    qwe = list(map(int,input().split()))
    li2.append(qwe)
    li22.append(qwe)

li3 = []
li3.append(c)
li5 = []
while len(li3) != 0:
    st = li3[0]
    if(not st in li5): print(st,end = ' ')
    li5.append(st)
    del li3[0]
    i = 0
    li4 = []
    while i != len(li2):
        for j in range(2):
            if(li2[i][j] == st):
                li4.append(li2[i][j*-1+1])
                del li2[i]
                i-=1
                break
        i+=1
    li4 = sorted(li4)
    li3 = li4+li3 
print()

li3 = []
li3.append(c)
li5 = []
while len(li3) != 0:
    st = li3[0]
    if(not st in li5): print(st,end = ' ')
    li5.append(st)
    del li3[0]
    i = 0
    li4 = []
    while i != len(li22):
        for j in range(2):
            if(li22[i][j] == st):
                li4.append(li22[i][j*-1+1])
                del li22[i]
                i-=1
                break
        i+=1
    li4 = sorted(li4)
    li3 = li3+li4 
print()