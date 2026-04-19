import sys
li = [1,2]
dum = 1
for i in range(191229):
    li.append((li[-1]+li[-2])%(1000000007))
for i in range(int(input())):
    sys.stdout.write(str(li[int(sys.stdin.readline())-1])+"\n")