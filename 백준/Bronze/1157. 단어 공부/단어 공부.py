a = input()
b = ['']*(123)
c = [0]*(123)
for i in range(len(a)):
    if a[i] in b:
        if(ord(a[i]) < 92):
            c[ord(a[i])+32]+= 1
        else:
            c[ord(a[i])]+= 1
    else:
        if(ord(a[i]) < 92):
            b[ord(a[i])+32] = chr(ord(a[i])+32)
            c[ord(a[i])+32] += 1
        else:
            b[ord(a[i])] = a[i]
            c[ord(a[i])] += 1

hi = 0
hi2 = 0
for i in range(len(c)):
    if(hi < c[i]):
        hi = c[i]
        hi2 = i

qwe = 0
for i in range(len(c)):
    if(hi == c[i] and hi2 != i):
        print('?')
        qwe = 1
        break
if(qwe == 0):
    print(chr(ord(b[hi2])-32))