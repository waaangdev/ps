"개미굴"

import sys

def tam(dr,da):
    dr[1].sort(key = lambda x:(x[2]))
    for i in range(len(dr[1])):
        print("--"*da+dr[1][i][2])
        tam(dr[1][i],da+1)

gemi_su = int(sys.stdin.readline())
r = [{},[],""]

for i in range(gemi_su):    
    inp = sys.stdin.readline().split()
    r1 = r 
    for j in range(1,int(inp[0])+1):
        if((inp[j] not in r1[0])):
            r1[0][inp[j]] = len(r1[1])
            r1[1].append([{},[],inp[j]])

        r1 = r1[1][r1[0][inp[j]]]
tam(r,0)

