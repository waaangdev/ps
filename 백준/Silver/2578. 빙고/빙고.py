import sys
li1=[]
for i in range(5):
    li1.append(list(map(int,sys.stdin.readline().split())))
li2 = [[0 for i in range(5)]for j in range(5)]
s = -1
for i in range(5):
    a = list(map(int,sys.stdin.readline().split()))
    if(s != -2):
        for j in range(len(a)):
            b= 0
            for k in range(len(li1)):
                for l in range(len(li1[k])):
                    if(a[j] == li1[k][l]):
                        li2[k][l] = 1
                        b = 1
                        break
                if(b == 1):
                    break
            s = -1
            
            s1 = 0
            
            c= 0
            for k in range(5):
                if(li2[k][k] == 0):
                    c=1
            if(c == 0):
                s1 +=1
                
            d = 0
            for k in range(5):
                if(li2[k][4-k] == 0):
                    d=1
            if(d == 0):
                s1 +=1

            for k in range(5):
                e1 = 0
                for l in range(5):
                    if(li2[k][l] == 0):
                        e1=1
                if(e1 == 0):
                    s1 +=1
                
            for k in range(5):
                e1 = 0
                for l in range(5):
                    if(li2[l][k] == 0):
                        e1=1
                if(e1 == 0):
                    s1 +=1
            
            if(s1 > 2):
                s = j
                break
            
        if(s != -1):
            print(i*5+(s)+1)
            s = -2