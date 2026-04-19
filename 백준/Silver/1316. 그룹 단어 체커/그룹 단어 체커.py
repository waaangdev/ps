a = int(input())
b = 0
g = 0
for i in range(a):
    c = input()
    d = []
    e = 0
    f = 0
    for j in range(len(c)):
        if c[j] in d:
            if e in d and e != c[j]:
                f = 1
                break
        else:
            d.append(c[j])
        
        e = c[j]
    if(f == 0):
        g += 1
print(g)