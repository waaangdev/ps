a = int(input())
num = []
for _ in range(a):
    num.append(list(map(int,input().split())))
for i in range(len(num)):
    d = 1
    for j in range(len(num)):
        if (num[i][0] < num[j][0] and num[i][1] < num[j][1]):
            d += 1
    print(d,end = ' ')