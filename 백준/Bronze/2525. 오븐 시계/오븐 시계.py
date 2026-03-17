a,b = map(int,input().split())
c = a*60+b+int(input())
print(c//60%24,c%60)