a = int(input())
b = list(map(int,input().split()))
c = int(input())
li = 0
d = c
e = c
while 1:
    e += 1
    if(e in b or d in b):
        break
    li += 1
d = c
e = c
li2 = 0
while 1:
    e -= 1
    if(e in b or e == 0 or d in b):
        break
    li2 += 1
    
print(li+(li2*li)+li2)