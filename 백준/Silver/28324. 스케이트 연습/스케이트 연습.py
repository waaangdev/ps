import sys
a = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
r = 0
his = 0
for i in li[::-1]:
    his = min(his+1,i)
    r+=his
print(r)