import sys

n = int(input())
t = int(input())
li = [[] for i in range(n)]
for i in range(t):
    x,y = (map(int,sys.stdin.readline().split()))
    li[x-1].append(y-1)
r = 0
dumli_prevs = dict()
for i in range(n):
    dumli = []
    li[i].sort()
    prev = -1
    li[i].append(n)
    for j in li[i]:
        if((j-prev) != 0):
            dumli.append([prev+1,j])
        prev = j
    dumli_prevs_dum = dict()
    for k in dumli:
        d2 = 1
        for j in (dumli_prevs):
            jv = dumli_prevs[j]
            #print(jv)
            for j2 in (jv):
                j2v = jv[j2]
                if(j2v < j2-j):
                    d = [max(j,k[0]),min(j2,k[1])]
                    if(d[1]-d[0] >= 0):
                        #if(j2v+1 <=d[1]-d[0]):
                        if(d[0] not in dumli_prevs_dum):dumli_prevs_dum[d[0]] = dict()
                        if(d[1] not in dumli_prevs_dum[d[0]]):dumli_prevs_dum[d[0]][d[1]] = 0
                        dumli_prevs_dum[d[0]][d[1]] = max(dumli_prevs_dum[d[0]][d[1]],min(j2v+1,d[1]-d[0]))

                        # dumli_prevs_dum.append(d+[j2[1]+1])
                        if(d == k):
                            d2 = 0
                        
        if(d2):
            d= k
            #print(d,dumli_prevs_dum)
            if(d[0] not in dumli_prevs_dum):dumli_prevs_dum[d[0]] = dict()
            if(d[1] not in dumli_prevs_dum[d[0]]):dumli_prevs_dum[d[0]][d[1]] = 0
            dumli_prevs_dum[d[0]][d[1]] = max(dumli_prevs_dum[d[0]][d[1]],1)


    dumli_prevs.clear()
    dumli_prevs= dumli_prevs_dum
    for j in (dumli_prevs):
        jv = dumli_prevs[j]
        for j2 in (jv):
            j2v = jv[j2]
            r = max(r,min(j2-j,j2v))

    #print(dumli,dumli_prevs)

print(r)