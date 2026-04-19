import sys

n = int(input())
s = sys.stdin.readline().strip()
s = ["ACGT".index(i) for i in s]
r = len(s)
for i in range(1,n+1):
    r2 = 0
    li = [[0,0,0,0] for i in range(i)]
    for j in range(len(s)):
        li[j%i][s[j]]+=1
    r=min(r,len(s)-sum([max(j) for j in li]))

print(r)