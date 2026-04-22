import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
li.sort(key=lambda x:n2%x)
print(li[0])