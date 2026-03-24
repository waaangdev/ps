n=int(input())
for i in list(range(n*2-1,0,-2))+list(range(3,n*2+1,2)):print(" "*((n*2-1-i)//2)+"*"*i)