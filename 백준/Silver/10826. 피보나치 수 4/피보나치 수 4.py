
li=[1,1]
n=int(input())
if(n==0):print(0)
else:
    for i in range(n):
        li+=[li[-2]+li[-1]]
    print(li[n-1])