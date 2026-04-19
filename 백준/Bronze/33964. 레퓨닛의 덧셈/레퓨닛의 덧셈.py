a,b = map(int,input().split())
if(a>b): a,b = b,a
print('1'*(b-a)+'2'*(a))