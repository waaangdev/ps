import sys

li = []
for i in range(5):
    a = int(sys.stdin.readline())
    if(a in li):
        li.remove(a)
    else:
        li.append(a)
print(li[0])