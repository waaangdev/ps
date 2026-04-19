n = int(input())
r = (0)
li =list(map(int,input().split()))
dum = 0
dum1 = 0
for i in li:
    r = r^(i)
    if(i==1): dum1+=1
if(dum1 == n):
    if(dum1%2 == 1):
        print("cubelover")
    else:
        print("koosaga")
elif(dum1 == n-1):
    print("koosaga")
else:
    if(r == 0):
        print("cubelover")
    else:
        print("koosaga")
