a = int(input())
for i in range(a):
    b = input()
    c = 0
    e = []
    for j in range(len(b)):
        if(b[j] == ')'):
            if(len(e) != 0):
                del e[len(e)-1]
            else:
                c = 1
        else:
            e.append(1)
    if(c == 0 and len(e) == 0):
        print('YES')
    else: print("NO")