import sys
a = int (input())
li = set([])
for i in range(a):
    li.add(sys.stdin.readline().strip())
li = list(li)
li.sort(key=lambda x:[len(x),x])
print("\n".join(li))