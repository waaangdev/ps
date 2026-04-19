ang = [[1,0],[0,1],[-1,0],[0,-1]]
r1 = ["yes",'no']
gen = [
       [1,2,3,4],
       [0,4,5,2],
       [0,1,5,3],
       [0,2,5,4],
       [0,3,5,1],
       [2,1,4,3]
       ]
for _ in range(3):
    li = [0 for i in range(6)]
    li2 = [[0 for j in range(6)] for i in range(6)]
    m = []
    for i in range(6):
        m.append(list(map(int,input().split())))
    br = 0
    for i in range(6):
        for j in range(6):
            if(m[i][j] == 1):
                li3 = [[i,j,i,j,0,0]] #현재위치,이전위치,현재숫자,이전숫자
                li2[i][j] = 1
                br = 1
                break
            
        if(br == 1): break
    r = 0
    li[0] = 1
    while 1:
        if(len(li3) == 0):
            break
        
        if(li3[0][4] != 0):

            ijang = 0
            for i in range(4):
                if(li3[0][0] + ang[i][0] >= 0 and li3[0][0] + ang[i][0] < 6 and li3[0][1] + ang[i][1] >= 0 and li3[0][1] + ang[i][1] < 6):
                    if(li3[0][0] + ang[i][0] == li3[0][2] and li3[0][1] + ang[i][1] == li3[0][3]):
                        ijang = i
                        break


            while gen[li3[0][4]][ijang] != li3[0][5]:
                gen[li3[0][4]].append(gen[li3[0][4]][0])
                del gen[li3[0][4]][0]

            
        for i in range(4):
            if(li3[0][0] + ang[i][0] >= 0 and li3[0][0] + ang[i][0] < 6 and li3[0][1] + ang[i][1] >= 0 and li3[0][1] + ang[i][1] < 6):
                if(m[li3[0][0] + ang[i][0]][li3[0][1] + ang[i][1]] == 1):
                    if(li2[li3[0][0] + ang[i][0]][li3[0][1] + ang[i][1]] == 0):
                        if(li3[0][4] == 0):
                            if(i == 0):
                                li3.append([li3[0][0] + ang[i][0],li3[0][1] + ang[i][1],li3[0][0],li3[0][1],2,0])
                                li2[li3[0][0] + ang[i][0]][li3[0][1] + ang[i][1]] = 1
                                
                                li[2] = 1
                            elif(i == 1):
                                li3.append([li3[0][0] + ang[i][0],li3[0][1] + ang[i][1],li3[0][0],li3[0][1],3,0])
                                li2[li3[0][0] + ang[i][0]][li3[0][1] + ang[i][1]] = 1
                                
                                li[3] = 1
                            else:
                                print("error")
                        else:
                            li2[li3[0][0] + ang[i][0]][li3[0][1] + ang[i][1]] = 1
                            if(li[gen[li3[0][4]][i]] == 1):
                                r =1
                                break
                            li[gen[li3[0][4]][i]] = 1
                            li3.append([li3[0][0] + ang[i][0],li3[0][1] + ang[i][1],li3[0][0],li3[0][1],gen[li3[0][4]][i],li3[0][4]])
                            
                        
                        
                            
                            
        del li3[0]

        if(r == 1):
            break
    print(r1[r])