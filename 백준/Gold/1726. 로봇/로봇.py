import sys
from collections import deque

a, b = list(map(int, input().split()))

m = [0b0 for i in range(a)]
ang2 = [0, 2, 3, 1]
ang = [[0,1],[-1,0],[0,-1],[1,0]]

for i in range(a):
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(b):
        if (inp[j] == 1):
            m[i] |= (1 << j)

st = list(map(int, sys.stdin.readline().split()))
for i in range(3):
    st[i] -= 1
st[2] = ang2[st[2]]

end = list(map(int, sys.stdin.readline().split()))
for i in range(3):
    end[i] -= 1
end[2] = ang2[end[2]]


q = deque([st[:]+[[]]])

t = 0
m2 = [[0b0 for i in range(a)] for i in range(4)]
br = 0

if(st == end):
    t = 0
else:
    while 1:
        t += 1
        lenq = len(q)
        if (lenq == 0):
            break
        for i in range(lenq):
            popo = q.popleft()

            for j in range(1, 4):
                if (popo[0] + ang[popo[2]][0]*j >= 0 and popo[0] + ang[popo[2]][0]*j < a and popo[1] + ang[popo[2]][1]*j >= 0 and popo[1] + ang[popo[2]][1]*j < b):

                    if (m2[popo[2]][popo[0] + ang[popo[2]][0]*j] & (1 << (popo[1] + ang[popo[2]][1]*j)) == 0):

                        if (m[popo[0] + ang[popo[2]][0]*j] & (1 << (popo[1] + ang[popo[2]][1]*j)) == 0):

                            if ([popo[0] + ang[popo[2]][0]*j, popo[1] + ang[popo[2]][1]*j, popo[2]] == end):
                                br = 1
                                break

                            q.append([popo[0] + ang[popo[2]][0]*j,popo[1] + ang[popo[2]][1]*j, popo[2],popo[3]+[popo[:3]]])

                            m2[popo[2]][popo[0] + ang[popo[2]][0] *j] |= (1 << (popo[1] + ang[popo[2]][1]*j))
                        else:
                            break

            for j in range(-1,2,2):
                if(m2[(popo[2]+j) % 4][popo[0]] & (1 << (popo[1])) == 0):
                    q.append([popo[0], popo[1], (popo[2]+j) % 4,popo[3]+[popo[:3]]])
                    m2[(popo[2]+j) % 4][popo[0]] |= (1 << (popo[1]))
                    if ([popo[0], popo[1], (popo[2]+j) % 4] == end):
                        br = 1
                        break
            if (br == 1):
                break
        if (br == 1):
            break
print(t)
