import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())
li = []
for i in range(n):
    li.append(list(map(int,sys.stdin.readline().strip().split())))
if((n*m)%2 == 0):
    print("Yes")
    if((n)%2 == 0):
        for i in range(n//2):
            for j in range(m):
                li[i*2][j],li[i*2+1][j] = li[i*2+1][j],li[i*2][j]
    else:
        for i in range(n):
            for j in range(m//2):
                li[i][j*2],li[i][j*2+1] = li[i][j*2+1],li[i][j*2]
    for i in range(n):
        print(*li[i])
else:
    print("No")
    # if(n == 1 and m == 1):
    #     print("No")
    # else:
    #     if((n) != 1):
    #         for i in range(n-1):
    #             li[i*2][j],li[i*2+1][j] = li[i*2+1][j],li[i*2][j]
    #         for i in range(n//2):
    #             for j in range(m):
    #                 li[i*2][j],li[i*2+1][j] = li[i*2+1][j],li[i*2][j]
    #     else:
    #         for i in range(m//2):
    #             for j in range(n):
    #                 li[i][j*2],li[i][j*2+1] = li[i][j*2+1],li[i][j*2]

