import sys
a = int(input())
for i in range(a):
    n = int(input())
    li = list(map(int,sys.stdin.readline().strip().split()))
    li2 = list(map(int,sys.stdin.readline().strip().split()))

    li.sort()
    li2.sort()
    li2.reverse()
    r = 0
    for j in range(n*4):
        r = max(r,li[j//4]+li2[j])
    print(f"Trip #{i+1}: {r}")

