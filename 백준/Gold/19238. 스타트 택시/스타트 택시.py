from collections import deque
import sys 

ang = [[-1,0],[0,1],[0,-1],[1,0]]

a,b,en = map(int,input().split())
m = []
for i in range(a):
    m.append(list(map(int,sys.stdin.readline().strip().split())))

pl = list(map(int,sys.stdin.readline().strip().split()))

pl[0] -=1
pl[1] -=1

m1 = [[0 for j in range(a)] for i in range(a)]
for i in range(b):
    r = list(map(int,sys.stdin.readline().strip().split()))
    m1[r[0]-1][r[1]-1] = [r[2]-1,r[3]-1]
    
for _ in range(b):

    if(m1[pl[0]][pl[1]] != 0): 
        li = [[pl[0],pl[1],m1[pl[0]][pl[1]],-1]]
    else:
            
        li = []
        find = deque([[pl[0],pl[1],0]])
        brbr = 0
        m2 = [[0 for j in range(a)] for i in range(a)]
        while len(find) != 0:
            find1 = len(find)
            for i in range(find1):
                find3 = find.popleft()
                for j in range(4):
                    find2 = [find3[0]+ang[j][0],find3[1]+ang[j][1],find3[2]]
                    if(find2[0] >= 0 and find2[0] < a and find2[1] >= 0 and find2[1] < a):
                        if(m1[find2[0]][find2[1]] != 0):
                            li.append([find2[0],find2[1],m1[find2[0]][find2[1]],find2[2]])
                            brbr = 1
                        elif(m[find2[0]][find2[1]] == 0 and m2[find2[0]][find2[1]] == 0):
                            find.append([find2[0],find2[1],find2[2]+1])
                            m2[find2[0]][find2[1]] = 1
            if(brbr == 1):
                break
        if(len(li) == 0):
            en = -1
            break
    max_li_1 = a*a+a
    max_li_2 = 0
    for i in range(len(li)):
        if(max_li_1 > li[i][0]*a+li[i][1]):
            max_li_1 = li[i][0]*a+li[i][1]
            max_li_2 = i
    m1[li[max_li_2][0]][li[max_li_2][1]] = 0
    en1 = li[max_li_2][3]+1
    pl = li[max_li_2][0:2]
    en -= en1
    if(en < 0):
        break
    en1 = 0
    find = deque([[pl[0],pl[1],0]])
    brbr = 0
    en2 = 0
    m2 = [[0 for j in range(a)] for i in range(a)]
    while len(find) != 0:
        find1 = len(find)
        for i in range(find1):
            find3 = find.popleft()
            for j in range(4):
                find2 = [find3[0]+ang[j][0],find3[1]+ang[j][1],find3[2]]
                if(find2[0] >= 0 and find2[0] < a and find2[1] >= 0 and find2[1] < a):
                    if(find2[0] == li[max_li_2][2][0] and find2[1] == li[max_li_2][2][1]):
                        en1 = find2[2]+1
                        en2 = [find2[0],find2[1]]
                        brbr = 1
                    elif(m[find2[0]][find2[1]] == 0 and m2[find2[0]][find2[1]] == 0):
                        find.append([find2[0],find2[1],find2[2]+1])
                        m2[find2[0]][find2[1]] = 1

        if(brbr == 1):
            break
    if(len(li) == 0):
        en = -1
        break
    if(en2 == 0):
        en = -1
        break
    en -= en1
    if(en < 0):
        break
    else:
        en+=en1*2

    pl = en2[:]

print(max(-1,en))