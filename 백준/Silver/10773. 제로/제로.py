a = int(input())
li = []
for i in range(a):
    c = int(input())
    if(c == 0):
        li.pop()
    else:
        li.append(c)
s = 0
for i in range(len(li)):
    s += li[i]
print(s)
        
