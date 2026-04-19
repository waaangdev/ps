a = list(map(int,input().split()))
a[1] = a[1]-45
if(a[1] < 0):
    a[1]+=60
    a[0] -= 1
if(a[0] == -1):
    a[0] = 23
print(*a)