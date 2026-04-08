def s(a):
    if(len(a) != n):
        a1 = ["" for i in range(len(a)*2)]
        q = len(a[0])*2+1
        for i in range(len(a1)):
            if i < len(a):
                a1[i] = ' '*((q-len(a[0]))//2) + a[i] + ' '*((q-len(a[0]))//2)
            else:
                a1[i] = a[i%len(a)] + ' ' + a[i%len(a)]
        if len(a1) != n: a1 = s(a1)
    else:
        a1 = a
    return a1

n = int(input())
r = s(['  *  ',
       ' * * ',
       '*****'])
for i in range(n):
    print(r[i])