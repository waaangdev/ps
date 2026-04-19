a,b = map(int,input().split())
li = list(map(int,input().split()))
for i in range(a):
    if(li[i] < b):
        print(li[i],end = ' ')