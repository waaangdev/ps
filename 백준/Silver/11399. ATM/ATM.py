a = int(input())
li = sorted(list(map(int,input().split())))
s = 0
s1 = 0
for i in range(a):
    s1 += li[i]
    s+=s1
print(s)