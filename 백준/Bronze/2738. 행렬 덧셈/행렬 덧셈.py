a,b = map(int,input().split())
li =[]
for i in range(a):
    li.append(list(map(int,input().split())))
for i in range(a):
    c = list(map(int,input().split()))
    for j in range(b):
        print(c[j]+li[i][j],end = ' ')
    print()