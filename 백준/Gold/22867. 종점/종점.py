a = int(input())
li = []
for i in range(a):
    dum = input().split()
    li.extend([[dum[0],1],[dum[1],-1]])
li.sort(key=lambda x: x[0])
b,r =0,0
for i in li:
    b += i[1]
    r = max(r,b)
print(r)