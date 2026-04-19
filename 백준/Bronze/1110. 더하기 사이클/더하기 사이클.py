n = input().zfill(2)
c= n
a = 0
while 1:
    n = n[1]+str(int(n[0]) + int(n[1])).zfill(2)[1]
    a += 1
    if (c == n):
        break
print(a)