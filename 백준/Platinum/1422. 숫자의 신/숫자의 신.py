from collections import deque
n,k = map(int,input().split())
li = [""]*n
for i in range(n):
    li[i] = input()

li_lmax = max([len(i) for i in li])
li_max = ""
li_max_i = 0
for i in range(n):
    if(len(li[i]) == li_lmax):
        if(li[i]>li_max):
            li_max = li[i]
            li_max_i = i
li += [li_max]*(k-n)
li2 = [i*li.count(i) for i in list(set(li))]
#print(li2)
lli2 = len(li2)
q = deque([[[False]*(lli2),""]])
maxstr = ""
for i in range(lli2):
    lenq = len(q)
    for j in range(lenq):
        qpop = q.popleft()
        for l in range(lli2):
            if(not qpop[0][l]):
                qpop[0][l] = True
                q.append([qpop[0][:],qpop[1]+li2[l]])
                qpop[0][l] = False

    lenq = len(q)
    q2 = list(q)
    q22 = [True]*lenq
    q = deque([])
    for j in range(10000000):
        maxx = ""
        dum = 0
        for l in range(lenq):
            if(len(q2[l][1]) > j and q22[l]):
                dum = 1
                maxx = max(q2[l][1][j],maxx)
        if(dum==0):break
        for l in range(lenq):
            if(len(q2[l][1]) > j and q22[l]):
                if(q2[l][1][j] != maxx):
                    q22[l] = False
    for l in range(lenq):
        if(q22[l]):
            q.append(q2[l])
print(list(q)[0][1])