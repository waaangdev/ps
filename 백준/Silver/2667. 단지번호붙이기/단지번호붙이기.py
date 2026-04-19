import sys
sys.setrecursionlimit(626)
a = int(input())
m = []
for i in range(a):
    m.append(list(input()))
cl = []
ll = [0,0,-1,1]
def ch(i,j):
    r=1
    for k in range(len(ll)):
        if(i+ll[k] > -1 and i+ll[k] < a and j+ll[-1-k] > -1 and j+ll[-1-k] < a):
            if(m[i+ll[k]][j+ll[-1-k]] == '1'):
                m[i+ll[k]][j+ll[-1-k]] ='0'
                r += ch(i+ll[k],j+ll[-1-k])
    return r
for i in range(a):
    for j in range(a):
        if(m[i][j] == '1'):
            m[i][j] ='0'
            cl.append(ch(i,j))
print(len(cl))
cl = sorted(cl)
for i in range(len(cl)):
    print(cl[i])