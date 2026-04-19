
#정렬하기
import sys
n = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
nums = sum([(li[i]==i)*1+0 for i in range(n)])
m = int(input())
for i in range(m):
    a,b = list(map(int,sys.stdin.readline().strip().split()))
    if(a!=b):
        nums -= (li[a]==a)*1
        nums -= (li[b]==b)*1
        li[a],li[b] = li[b],li[a]
        nums += (li[a]==a)*1
        nums += (li[b]==b)*1
    if(li == [1,0]):
        print(1,end=' ')
    else:print((nums==n)*1-1,end=' ')