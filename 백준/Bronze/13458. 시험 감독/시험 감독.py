import sys
a = int(input())
li = list(map(int,sys.stdin.readline().split()))
b,c= (map(int,sys.stdin.readline().split()))
r = 0
for i in range(a):
    li[i] -= b
    li[i] = max(0,li[i])
    r += ((li[i]+(c-1))//c)+1
print(r)