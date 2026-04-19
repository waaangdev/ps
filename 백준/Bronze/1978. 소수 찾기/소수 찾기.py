input()
a = sorted(list(map(int,input().split())))
b = a[len(a)-1]
for i in range(2,b):
    j=0
    while 1:
        if(len(a) == j or len(a) == 0):
            break
        if((a[j] % (i) == 0 and a[j] != i) or a[j] == 1):
            del a[j]
        else:
            j += 1
print(len(a))