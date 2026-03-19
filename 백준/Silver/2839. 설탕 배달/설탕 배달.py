n = int(input())
a = 0
b = 0
c = 0
if((n) % 5 == 0):
    c = n//5
else:
    while 1:
        if((n - a*5) % 3 == 0 and (n) % 5 != 0):
            if((n - a*5) // 3 > 0): b = (n - a*5) // 3
            if(c > a+b or c == 0):
                c = a+b
        a += 1
        if(a*5 > n):
            break
if(c <= 0): print(-1)
else:print(c)