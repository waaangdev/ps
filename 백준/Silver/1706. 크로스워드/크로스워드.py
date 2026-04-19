a,b = map(int,input().split())
li = []
r = ['z' for i in range(21)]
for i in range(a):
    li.append(input())


for i in range(a):
    pointer = 0
    min_ = 0
    r2 = []
    for j in range(b):

        if(li[i][j] != '#'):
            if(min_ == 0):
                if(pointer >= len(r)):
                    min_ = 2
                else:
                    if(ord(li[i][j]) < ord(r[pointer])):
                        min_ = 1
                    elif(ord(li[i][j]) > ord(r[pointer])):
                        min_ = 2

            r2.append(li[i][j])
            pointer += 1

        else:
            if (min_ <= 1 and pointer > 1):
                r = r2[:]
            r2 = []
            pointer = 0
            min_ = 0
    if (min_ <= 1 and pointer > 1):
        r = r2[:]
for j in range(b):
    pointer = 0
    min_ = 0
    r2 = []
    for i in range(a):

        if (li[i][j] != '#'):
            if (min_ == 0):
                if (pointer >= len(r)):
                    min_ = 2
                else:
                    if (ord(li[i][j]) < ord(r[pointer])):
                        min_ = 1
                    elif (ord(li[i][j]) > ord(r[pointer])):
                        min_ = 2

            r2.append(li[i][j])
            pointer += 1

        else:
            if (min_ <= 1 and pointer > 1):
                r = r2[:]
            r2 = []
            pointer = 0
            min_ = 0
    if (min_ <= 1 and pointer > 1):
        r = r2[:]

print(''.join(r))