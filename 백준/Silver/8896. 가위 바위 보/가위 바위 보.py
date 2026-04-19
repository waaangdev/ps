import sys
#from collections import deque
n = int(input())
for i in range(n):
    r = int(input())
    li = []
    for j in range(r):
        li.append([input(),j+1])
    for j in range(len(li[0][0])):
        rcp = []
        for k in range(len(li)):
            if(not li[k][0][j] in rcp):
                rcp.append(li[k][0][j])
            if(len(rcp) == 3):
                break
        if(len(rcp) == 2):
            if('R'in rcp and 'P'in rcp):
                k = 0
                while k != len(li):
                    if(li[k][0][j] == 'R'):
                        del li[k]
                    else:
                        k += 1
            if('S'in rcp and 'R'in rcp):
                k = 0
                while k != len(li):
                    if(li[k][0][j] == 'S'):
                        del li[k]
                    else:
                        k += 1
            if('P' in rcp and 'S'in rcp):
                k = 0
                while k != len(li):
                    if(li[k][0][j] == 'P'):
                        del li[k]
                    else:
                        k += 1
    if(len(li) == 1):
        print(li[0][1])
    else:
        print(0)