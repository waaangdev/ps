import sys
a = int(input())
input()
li = list(map(int,input().split()))
sa = []
for i in range(len(li)):
    t = 0
    for j in range(len(sa)):
        if(li[i] == sa[j][0]):
            sa[j][1] +=1
            t = 1
            break
    if(t == 0):
        if(len(sa) == a):
            ch = 0
            ch1 = 0
            for j in range(len(sa)):
                if(sa[j][1]<ch or j == 0):
                    ch = sa[j][1]
                    ch1 = j
            del sa[ch1]
        sa.append([li[i],1])
print(*sorted([i[0] for i in sa]))