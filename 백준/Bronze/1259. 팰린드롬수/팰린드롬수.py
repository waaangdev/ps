while 1:
    a = int(input())
    if(a ==0):
        break
    if(len(str(a)) % 2 == 0):
        c = 0
        for i in range(len(str(a))//2):
            if(str(a)[i] == str(a)[-i-1]):
                pass
            else:
                c = 1
                break
    else:
        c = 0
        for i in range(len(str(a))//2):
            if(str(a)[i] == str(a)[-i-1]):
                pass
            else:
                c = 1
                break
    if(c):
        print('no')
    else:
        print('yes')
        