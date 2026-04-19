import sys

a = int(sys.stdin.readline())

for _ in range(a):
    li = [0 for i in range(8)]
    for i in range(3):
        inp = sys.stdin.readline().strip()
        if(i == 0):
            for j in range(3):
                li[j] = inp[j]
        if(i == 1):
            li[7] = inp[0]
            li[3] = inp[2]
        if(i == 2):
            for j in range(3):
                li[2-j+4] = inp[j]
    
    cmd = list(map(int,sys.stdin.readline().split()))
    li.append(li[0])
    r = []
    dum = 0
    for i in range(8):
        if(li[i] == 'O'):
            dum+=1
            if(i==7):
                if(li[8] == 'O'):
                    if(r == []):
                        r.append(dum)
                    else:
                        r[0] += dum
                else:
                    r.append(dum)

        if(li[i] == 'X'):
            if(dum != 0):
                r.append(dum)
            dum = 0
    del cmd[0]
    r.sort()
    if(cmd == r):
        print(1)
    else:
        print(0)