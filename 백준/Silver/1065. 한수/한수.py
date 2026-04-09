a = int(input())
c = 0
for i in range(1,a+1):
    if(len(str(i)) < 3):
        c+= 1
    if(len(str(i)) > 2):
        q = int(str(i)[1]) - int(str(i)[0])
        b = 0
        for j in range(len(str(i))-1):
            if(int(str(i)[j+1]) - int(str(i)[j]) != q):
                b = 1
        if(b == 0):
            c+=1
print(c)