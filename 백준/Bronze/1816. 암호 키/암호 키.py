n = int(input())
r = 0
for _ in range(n):
    num = (int(input()))
    r = 0
    for i in range(2,1000001):
        if(num%i == 0):
            r = 1
    print("YES"*(1-r)+"NO"*(r))