import sys
a,b,c = map(int,input().split())
m = []
m2 = {'O':0,'.':-1}
def p(q):
    if(q < 0):
        return '.'
    else:
        return 'O'
for i in range(a):
    m.append([m2[i] for i in list(sys.stdin.readline().strip())])
if(c%2 == 0):
    for i in range(a):
        for j in range(b):
            print("O",end = '')
        print()
elif (c == 1):
    for i in range(a):
        for j in range(b):
            print(p(m[i][j]),end = '')
        print()
elif ((c)%4 == 1):
    t = 1
    for _ in range(2):
        t+=2
        for i in range(a):
            for j in range(b):
                if(m[i][j] < 0 and m[i][j] != -t):
                    m[i][j] = t-1

                if(m[i][j] == t-3):
                    m[i][j] = -1
                    if(i-1 >= 0 and m[i-1][j] != t-3):m[i-1][j] = -t
                    if(i+1 < a and m[i+1][j] != t-3):m[i+1][j] = -t
                    if(j-1 >= 0 and m[i][j-1] != t-3):m[i][j-1] = -t
                    if(j+1 < b and m[i][j+1] != t-3):m[i][j+1] = -t
    for i in range(a):
        for j in range(b):
            print(p(m[i][j]),end = '')
        print()
elif ((c)%4 == 3):
    t = 1
    for _ in range(1):
        t+=2
        for i in range(a):
            for j in range(b):
                if(m[i][j] < 0 and m[i][j] != -t):
                    m[i][j] = t-1

                if(m[i][j] == t-3):
                    m[i][j] = -1
                    if(i-1 >= 0 and m[i-1][j] != t-3):m[i-1][j] = -t
                    if(i+1 < a and m[i+1][j] != t-3):m[i+1][j] = -t
                    if(j-1 >= 0 and m[i][j-1] != t-3):m[i][j-1] = -t
                    if(j+1 < b and m[i][j+1] != t-3):m[i][j+1] = -t
    for i in range(a):
        for j in range(b):
            print(p(m[i][j]),end = '')
        print()