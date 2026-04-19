input()
a = [[i,0,0] for i in reversed(list(input()))]
b = [[i,1,0] for i in list(input())]
li = a+b
t = int(input())
for k in range(t):
    for i in range(len(li)):
        if(li[i][2] <= k):
            if(li[i][1] == 1 and i != 0):
                if(li[i-1][1] == 0 and li[i-1][2] <= k):
                    li[i][2] = k+1
                    li[i-1][2] = k+1
                    c = li[i]
                    li[i] = li[i-1]
                    li[i-1] = c
            if(li[i][1] == 0 and i != len(li)-1):
                if(li[i+1][1] == 1 and li[i+1][2] <= k):
                    li[i][2] = k+1
                    li[i+1][2] = k+1
                    c = li[i]
                    li[i] = li[i+1]
                    li[i+1] = c
for i in li:
    print(i[0],end = '')