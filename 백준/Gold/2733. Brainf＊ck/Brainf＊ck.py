a = int(input())
for i in range(a):
    li = [0 for _ in range(32768)]
    li_pointer = 0
    
    prpr = ''
    er = 0
    b = ''
    j = 0
    while 1:
        b1 = input()
        try:
            b1 = b1[:b1.index('%')]
        except:
            pass
        if(b1 == 'end'):
            break
        else:
            b += b1
    while (j < len(b)):
        if(b[j] == '>'):
            li_pointer += 1
            if(li_pointer == 32768):
                li_pointer = 0
        elif(b[j] == '<'):
            li_pointer += -1
            if(li_pointer == -1):
                li_pointer = 32767
        elif(b[j] == '+'):
            li[li_pointer] += 1
            if(li[li_pointer] == 256):
                li[li_pointer] = 0
        elif(b[j] == '-'):
            li[li_pointer] -= 1
            if(li[li_pointer] == -1):
                li[li_pointer] = 255
        elif(b[j] == '.'):
            prpr += chr(li[li_pointer])
        elif(b[j] == ']'):
            
            e = 0
            for k in range(j-1,-1,-1):
                if(b[k] == ']'):
                    e+=1
                elif(b[k] == '['):
                    e-=1
                    if(e == -1):
                        if(li[li_pointer] != 0):
                            j = k
                        break
            if(e != -1):
                er = 1
                break
        elif(b[j] == '['):
            e = 0
            for k in range(j+1,len(b)):
                if(b[k] == '['):
                    e+=1
                elif(b[k] == ']'):
                    e-=1
                    if(e == -1):
                        if(li[li_pointer] == 0):
                            j = k
                        break
            if(e != -1):
                er = 1
                break
        j+=1
    print("PROGRAM #"+str(i+1)+":")
    if(er == 0):
        print(prpr)
    else:
        print('COMPILE ERROR')