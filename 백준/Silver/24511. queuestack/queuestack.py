from collections import deque
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
result = deque()
for i in range(n):
    if a[i] == 0: result.append(b[i])
for i in range(m):
    result.appendleft(c[i])
    print(result.pop(), end=" ")