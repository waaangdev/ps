a,b = map(int,input().split())
n = int(input())
r = "YES"
for i in range(n):
    input()
    if(b not in list( map(int,input().split()))):
        r = "NO"
print(r)