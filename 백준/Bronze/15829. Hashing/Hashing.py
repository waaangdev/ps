input()
l = input()
r = 0
r2 = 1
for i in range(len(l)):
    r=(r+r2*(ord(l[i])-ord('a')+1))%1234567891
    r2=(r2*31)%1234567891
print(r)