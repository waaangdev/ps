a,b,c = map(int,input().split())
d = a*60*60+b*60+c+int(input())
print(round(d//60//60%24),round(d//60%60),d%60)