a = int(input())
for i in range(a):
    li = list(reversed((sorted(list(map(int,input().split()))))))
    print(li[2])