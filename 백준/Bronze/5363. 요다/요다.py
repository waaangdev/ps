a = int(input())
for i in range(a):
    b = input().split()
    b.append(b[0])
    del b[0]
    b.append(b[0])
    del b[0]
    for j in b:
        print(j,end = ' ')
    print('')
