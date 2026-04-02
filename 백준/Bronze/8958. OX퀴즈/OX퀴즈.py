d = int(input())
for j in range(d):
    a = input()
    b = 0
    c = 0
    for i in range(len(a)):
        if(a[i] == 'O'):
            b += 1
        else:
            b = 0
        c += b
    print(c)