b,x,k=list(map(int,input().split()))
for i in range(k):
    a,b = list(map(int,input().split()))
    if(x == a):x=b
    elif(x==b):x=a
print(x)