a,b=map(int,input().split())
print(max([int(str(i*a)[::-1]) for i in range(1,b+1)]))