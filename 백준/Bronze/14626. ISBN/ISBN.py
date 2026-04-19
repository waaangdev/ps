a= list(input())
b = 0
c = 0
for i in range(len(a)-1):
    if(a[i] == "*"):
        b = i


for j in range(10):
    a[b] = j
    c = 0
    for i in range(len(a)-1):
        c+= int(a[i])*(1+(i%2 == 1)*2)

    if((c+int(a[len(a)-1]))%10 == 0):
        print(j)
        break
