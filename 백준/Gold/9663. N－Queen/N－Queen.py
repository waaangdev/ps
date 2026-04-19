a= int(input())
r=0

li=[False for _ in range(a)]
li2=[False for _ in range(a*2)]
li3=[False for _ in range(a*2)]

def nq(q):
    global r
    if(q == 0): 
        r+=1
        return 0
    for i in range(a):
        if(li[i]): continue
        if(li2[i+(a-q)]): continue
        if(li3[(a-i-1)+(a-q)]): continue
        li[i] = True
        li2[i+(a-q)] = True
        li3[(a-i-1)+(a-q)] = True
        #print((a-q)*'-',i)
        nq(q-1)
        li[i] = False
        li2[i+(a-q)] = False
        li3[(a-i-1)+(a-q)] = False
    return 0

nq(a)
print(r)