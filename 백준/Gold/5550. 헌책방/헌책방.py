#헌책방
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().strip().split())

books = [[] for i in range(10)]
ptrs = [0]*10

for i in range(n):
    price,genre = map(int,sys.stdin.readline().strip().split())
    books[genre-1].append(price)

for i in range(10):
    books[i].sort()
    books[i].reverse()
    for j in range(1,len(books[i])):
        books[i][j] += books[i][j-1]

    for j in range(len(books[i])):
        books[i][j] += j*(j+1)
    books[i].insert(0,0)

# k2 = k
# for i in range(10):
#     ptrs[i] = min(k2,len(books[i])-1)
#     k2 -= ptrs[i]
#books = [[0, 100], [0, 14, 29, 44, 100000000,100000001], [0,100], [0,1,10000000], [0,1], [0], [0], [0], [0], [0]]

dp = [[-1 for i in range(2000)]for i in range(10)]
#print(books)
def sol(idx,k):
    if(dp[idx][k] != -1):
        return dp[idx][k]
    if(idx == 9):
        if(k >= len(books[idx])):
            return 0
        return books[idx][k]
    r = 0
    for i in range(min(k+1,len(books[idx]))):
        r = max(r,sol(idx+1,k-i)+books[idx][i])
    dp[idx][k] = r
    #print(idx,used,r)  
    return r

print(sol(0,k))