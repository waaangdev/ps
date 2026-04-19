import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

for _ in range(1):

    li = sys.stdin.readline().strip()

    rl = ""

    c = [li.count("A"),li.count("B"),li.count("C")]
    #print(c)
    abc = min(c)

    r = 1

    for i in range(3):
        c[i]-=abc

    if(c[0] == 0):
        if(c[2] == 0):
            if(c[1]<=abc+1):
                if(c[1]==abc+1):
                    for i in range(abc):
                        rl+="BCBA"
                    rl+="B"
                else:
                    for i in range(c[1]):
                        rl+="BCBA"
                    for i in range(abc-c[1]):
                        rl+="CBA"
                pass
            else:
                r=0
        elif(c[2] == 1):
            #print(1)
            if(c[1]<=abc+2):
                dum = min(c[1],abc)
                c[1]-=dum
                for i in range(dum):
                    rl+="BCBA"
                for i in range(abc-dum):
                    rl+="CBA"
                if(c[1] == 1):
                    rl+="CB"
                elif(c[1] == 2):
                    rl+="BCB"
                elif(c[1] == 0):
                    rl+="C"
                pass
            else:
                r=0
        else:
            r=0
    elif(c[1] == 0):
        caa = 0
        while (c[0] >= 2 and c[2]>=1):
            caa+=1
            c[0] -= 2
            c[2] -= 1

        for i in range(abc):
            rl+="CBA"
        for i in range(caa):
            rl+="CAA"
        if(c[2] == 0):
            pass
        elif(c[2] == 1):
            rl+="C"
            pass
        else:
            r = 0
        rl+="A"*c[0]
    elif(c[2] == 0):
        if(c[1] <= abc):
            for i in range(c[1]):
                rl+="BCBA"
            for i in range(abc-c[1]):
                rl+="CBA"
            rl+="A"*c[0]
            pass
        else:
            c[1] -= abc
            for i in range(abc):
                rl+="BCBA"
            dum = min(c[1],c[0])
            for i in range(dum):
                rl+="BA"
            c[1]-=dum
            c[0]-=dum
            if(c[0] ==0):
                if(c[1] <= 1):
                    if(c[1] == 1):rl+="B"
                    pass
                else:
                    r = 0
            else:
                rl+="A"*c[0]
                pass


    if(r):
        print(rl)
        if(len(li) != len(rl)):
            #print("ㅂ ㅅ")
            break
    else:
        print(-1)

