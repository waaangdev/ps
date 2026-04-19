n,m,s = map(int,input().split())
print(min(s*(100-n)*(m+1)//100,s*m))