a,b,v = map(int,input().split())
r = ((v-a)//(a-b))
dum = ((v-a)%(a-b))
if(dum == 0):
    print(r+1)
else:
    print(r+2)