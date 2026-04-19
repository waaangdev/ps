a = int(input())
c = ""
for j in range(a):
    b = input()
    if (j==0):
        c = b[:]
    if (j!=0):
        for i in range(len(c)):
            if (c[i] != b[i]):
                c = list(c)
                c[i] = '?'
                c = ''.join(c)
print(c)