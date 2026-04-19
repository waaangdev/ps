import sys
s= sys.stdin.readline().strip()
pal=1
sam = 1
for i in range(len(s)//2):
    if(s[i]!=s[-(i+1)]):
        pal=0
        sam=0
    if(s[i]!=s[len(s)//2]):
        sam=0
if(sam):
    print(-1)
elif(pal):
    print(len(s)-1)
else:
    print(len(s))