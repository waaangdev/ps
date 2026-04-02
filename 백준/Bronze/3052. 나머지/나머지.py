li = []
s = 0
e = 0
for i in range(10):
    e = int(input())%42
    if(not e in li):
        s+= 1
    li.append(e)
print(s)