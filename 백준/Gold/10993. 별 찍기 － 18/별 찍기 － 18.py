q = int(input())
def a(b):
    if(b == 1):
        return ['*']
    else:
        qwe = a(b-1)
        re = []
        if(b%2 == 1):
            re.append((len(qwe)*2)*' '+'*'+(len(qwe)*2)*' ')
            for i in range(len(qwe)*2-1-1,-1,-1):
                if(i<len(qwe)):
                    re.append((i+1)*' '+'*'+(len(qwe)-1-i)*' '+qwe[-1-i]+(len(qwe)-1-i)*' '+'*'+(i+1)*' ')
                else:
                    re.append((i+1)*' '+'*'+((len(qwe)*2-1-i)*2-1)*' '+'*'+(i+1)*' ')
            re.append(((len(qwe)*2)*2+1)*'*')
        else:
            re.append(((len(qwe)*2)*2+1)*'*')
            for i in range(len(qwe)*2-1):
                if(i<len(qwe)):
                    re.append((i+1)*' '+'*'+(len(qwe)-1-i)*' '+qwe[i]+(len(qwe)-1-i)*' '+'*'+(i+1)*' ')
                else:
                    re.append((i+1)*' '+'*'+((len(qwe)*2-1-i)*2-1)*' '+'*'+(i+1)*' ')
            re.append((len(qwe)*2)*' '+'*'+(len(qwe)*2)*' ')
        return re
rl = a(q)
for i in rl:
    for j in range(len(i)-1,-1,-1):
        if(i[j]=='*'):
            print(i[:j+1])
            break