from collections import deque
import copy

n,m = map(int,input().split())
bang = [-1 for i in range(1594323)]

str2bangli = [[0 for i in range(3)] for i in range(13)]
for i in range(13):
    for j in range(3):
        str2bangli[i][j] = j*(3**i)

zegop = [0 for i in range(13)]
for i in range(13):
    zegop[i] = 3**i

def str2bang(text):
    dum = 0
    for i in range(n):
        dum += str2bangli[i][text[i]]
    return dum
for _ in range(m):
    inp = list(input())
    inp2 = []
    abc = [0,0,0]
    for i in range(n):
        abc["ABC".index(inp[i])] += 1
        inp2.append("ABC".index(inp[i]))
    li = [0]*abc[0]+[1]*abc[1]+[2]*abc[2]

    if(inp2 == li):
        print(0)
        continue
    if(bang[str2bang(inp2)] != -1):
        print(bang[str2bang(inp2)])
        continue
    q = deque([str2bang(li)])
    bang[str2bang(li)] = 0
    t = 1
    while 1:
        lenq = len(q)
        if(lenq == 0):
            break
        for i in range(lenq):
            dumli = q.popleft()
            dumli2 = dumli%3
            dumli -= dumli2
            for j in range(1,n):
                dum = (dumli // zegop[j])%3
                dumli -= dum*zegop[j]
                dumli2 *= 3
                dumli2+=dum
                if(bang[dumli+dumli2] == -1 or bang[dumli+dumli2] > t):
                    bang[dumli+dumli2] = t
                    q.append(dumli+dumli2)
        t +=1
    print(bang[str2bang(inp2)])

