
a = int(input())
c =0
for i in range(a):
    b = 0
    for j in str(i):
        b+=int(j)
    if(i+b == a):
        c = 1
        d = i
        break
print(i*c)