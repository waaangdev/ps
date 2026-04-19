def add(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    if(n == 3):
        return 4
    return add(n-1)+add(n-2)+add(n-3)
a = int(input())
for i in range(a):
    print(add(int(input())))