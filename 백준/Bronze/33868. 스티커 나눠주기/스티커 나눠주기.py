n=int(input())
li=[0]*n
li2=[0]*n
for i in range(n):
    li[i],li2[i]=map(int,input().split())
print((min(li2)*max(li))%7+1)