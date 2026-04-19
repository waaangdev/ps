e = int(input())
if(0==e):
    r = 0
else:
    a = 1
    r = 1
    while 1:
        if(a>=e):
            break
        a *= 2
        r += 1
print(r)