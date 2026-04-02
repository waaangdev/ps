q = 0
for i in range(9):
    s = int(input())
    if(s > q):
        q = s
        q1 = i
print(q)
print(q1+1)