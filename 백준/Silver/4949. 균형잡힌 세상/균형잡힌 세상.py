import sys
while 1:
    li2 = sys.stdin.readline()
    if(li2 == ".\n"):
        break
    else:
        li = []
        for i in range(len(li2)):
            if(li2[i] == '(' or li2[i] == '['):
                li.append(li2[i])
            if(li2[i] == ')'):
                if(len(li) != 0):
                    if(li[len(li)-1] == '('):
                        li.pop()
                    else:
                        li.append(li2[i])
                        break
                else:
                    li.append(li2[i])
                    break
            if(li2[i] == ']'):
                if(len(li) != 0):
                    if(li[len(li)-1] == '['):
                        li.pop()
                    else:
                        li.append(li2[i])
                        break
                else:
                    li.append(li2[i])
                    break
        if(len(li) == 0):
            print('yes')
        else:
            print('no')
        