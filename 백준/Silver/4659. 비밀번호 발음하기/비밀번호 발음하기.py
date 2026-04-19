a = ['a','e','i','o','u']
while 1:
    b = input()
    if(b == 'end'):
        break
    else:
        c = 0
        c1 = 0
        d = 0
        e = ''
        e1 = 0
        for i in range(len(b)):
            if(b[i] in a):
                c1 += 1
                c +=1
                d = 0
            else:
                d+=1
                c = 0
            if (b[i] == e and e !='e' and e !='o'):
                e1 = 1
                break
            if(c == 3 or d == 3):
                e1 = 1
                break
            e = b[i]
        if(e1 == 0 and c1 != 0):
            print('<'+str(b)+"> is acceptable.")
        else:
            print('<'+str(b)+"> is not acceptable.")
            