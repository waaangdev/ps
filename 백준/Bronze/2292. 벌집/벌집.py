e = int(input())
li = 1
for i in range(e+1):
    if(e <= li):
        if(i == 0):
            print(i+1)
            break
        print(i)
        break
    li+=6*i