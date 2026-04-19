import sys
s = sys.stdin.readlines()
a = "aiyeou"
b = "bkxznhdcwgpvjqtsrlmf"
aa = [chr(ord(i)-32) for i in a]
bb = [chr(ord(i)-32) for i in b]
ab = "aiyeoubkxznhdcwgpvjqtsrlmf"
c = {ord(a[i]):i for i in range(6)}
d = {ord(b[i]):i for i in range(20)}
f = {ord(ab[i]):i for i in range(26)}
#print(c,d)
for j in s:
    for i in j:
        e = ord(i)
        #print(i)
        if(e < 91 and e > 64):
            if(f[e+32] < 6):
                print(aa[(c[e+32]+3)%6],end = "")
            else:
                print(bb[(d[e+32]+10)%20],end = "")
        elif(e < 123 and e > 96):
            if(f[e] < 6):
                print(a[(c[e]+3)%6],end = "")
            else:
                print(b[(d[e]+10)%20],end = "")
        else:
            print(i,end = "")
    
