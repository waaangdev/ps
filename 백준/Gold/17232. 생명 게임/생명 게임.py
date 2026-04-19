import sys
a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
m = [[0 for i in range(b)] for i in range(a)]
pp = '.*'
for i in range(a):
    inp = sys.stdin.readline()
    for j in range(b):
        if(inp[j] == '*'):
            m[i][j] = 1
m1 = [list(m[i]) for i in range(a)]
for i in range(c):
    mm = [[0 for i in range(b)] for i in range(a)]
    for j in range(a):
        for k in range(b):
            if(j == 0 and k == 0):
                ju = 0
                for l in range(-d,d+1):
                    for o in range(-d,d+1):
                        if(j+l > -1 and j+l < a and k+o > -1 and k+o < b):
                            ju += m[j+l][k+o]
                mm[j][k] = ju
            elif(k == 0):
                ju = mm[j-1][k]
                for o in range(-d,d+1):
                    if(j-1-d > -1 and j-1-d < a and k+o > -1 and k+o < b):
                        ju -= m[j-1-d][k+o]
                for o in range(-d,d+1):
                    if(j+d > -1 and j+d < a and k+o > -1 and k+o < b):
                        ju += m[j+d][k+o]
                mm[j][k] = ju
            else:
                ju = mm[j][k-1]
                for o in range(-d,d+1):
                    if(j+o > -1 and j+o < a and k-1-d > -1 and k-1-d < b):
                        ju -= m[j+o][k-1-d]
                for o in range(-d,d+1):
                    if(j+o > -1 and j+o < a and k+d > -1 and k+d < b):
                        ju += m[j+o][k+d]
                mm[j][k] = ju
            if (m[j][k] == 0):
                if(ju > e and ju <= f):
                    m1[j][k] = 1
            else:
                ju -= 1
                if(ju >= e and ju <= f):
                    m1[j][k] = 1
                elif(ju < e or ju > f):
                    m1[j][k] = 0
    m = [list(m1[i]) for i in range(a)]
for j in range(a):
    for k in range(b):
        print(pp[m[j][k]],end = '')
    print()