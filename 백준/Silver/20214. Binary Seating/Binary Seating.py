n=int(input())
li=list(map(int,input().split()))
li.sort()
r=0
for i in range(n):
    r+=2**i*li[i]
print(r/2**n)