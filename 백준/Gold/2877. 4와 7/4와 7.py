n = int(input())
dum = 2
dum2 = 0
dum3 = 1
while 1:
    if(n > dum2):
        dum2 += dum
        dum*=2
        dum3 += 1
    else:
        dum//=2
        dum2 -= dum
        dum3 -= 1
        break
# print(dum,dum2,dum3)
# print(n-dum2-1)
dum4 = n-dum2-1
for i in range(dum3-1,-1,-1):
    
    print([4,7][(dum4//pow(2,i))%(2)],end='')
