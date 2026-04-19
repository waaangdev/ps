import sys
n,m,q = map(int,input().split())#입력층개슈,은닉층개수,테케수
li1 = [[0 for i in range(n+1)] for i in range(m)]#은닉층[편향값,입력층 1 가중치,입력층 2 가중치,...]
li3 = [0 for i in range(m+1)]#출력층[편향값,은닉층 1 가중치,은닉층 2 가중치,...]

#은닉층 입력
for i in range(m):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    for j in range(inp[0]):
        li1[i][inp[j+1]] = inp[j+1+inp[0]]
    li1[i][0] = inp[len(inp)-1]
    
    
#출력층 입력
inp = list(map(int,sys.stdin.readline().strip().split()))
    
li3 = [inp[len(inp)-1]]+inp[0:len(inp)-1]

r1 = li3[0]

li2 = [0 for i in range(n+1)]

for i in range(m):
    for k in range(n):
        li1[i][k+1] *= li3[i+1]
        li2[k+1] += li1[i][k+1]
    
    r1 += li1[i][0]*li3[i+1]

for i in range(q):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    r = r1
    for k in range(n):
        r += inp[k] * li2[k+1]

    print(r)