li = [1 for i in range(30)]
for i in range(28):
    a = int(input())
    li[a-1] = 0
for i in range(30):
    if(li[i] == 1):
        print(i+1)