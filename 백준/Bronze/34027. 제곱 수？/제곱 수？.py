import math
for i in range(int(input())):
    a=int(input())
    if math.sqrt(a)==round(math.sqrt(a)):
        print(1)
    else:
        print(0)