import math
a = int(input())
for i in range(a):
    inp = int(input())
    r = 0
    for j in range(1,21):
        r+=inp//pow(5,j)
    print(r)

