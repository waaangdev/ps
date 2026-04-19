import math
a = int(input())
li = []
for i in range(a):
    li.append(list(map(float,input().split())))
b = int(input())
for i in range(b):
    c= int(input())
    inp = list(map(int,input().split()))
    r= 0
    for j in range(1,c):
        r += math.sqrt((li[inp[j-1]][0]-li[inp[j]][0])**2+(li[inp[j-1]][1]-li[inp[j]][1])**2)
    print(round(r))    
