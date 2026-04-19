import sys
n = int(input())

li = [0,0]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li[0] += a
    li[1] += b
li2 = [0,0]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li2[0] += a
    li2[1] += b
print((li2[0]-li[0])//n,(li2[1]-li[1])//n)