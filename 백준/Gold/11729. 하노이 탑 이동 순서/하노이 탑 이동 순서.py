n = int(input())

def h2(num,num2):
    if(num2 == 2):
        if(num == 1):
            return 3
        if(num == 3):
            return 1
    if(num2 == 1):
        if(num == 2):
            return 3
        if(num == 3):
            return 2
    if(num2 == 3):
        if(num == 2):
            return 1
        if(num == 1):
            return 2

def h(a,b,c):
    if(a == 1):
        print(b,c)
    else:
        h(a-1,b,h2(b,c))
        print(b,c)
        h(a-1,h2(b,c),c)

def h3(num):
    if(num == 1):
        return 1
    return h3(num-1)*2+1


print(h3(n))
h(n,1,3)