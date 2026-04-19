import sys

li = [0 for i in range(10000)]
for i in range(int(input())):
    li[int(input())-1] += 1
for i in range(1,10001):
    for j in range(li[i-1]):
        sys.stdout.write(str(i)+"\n")