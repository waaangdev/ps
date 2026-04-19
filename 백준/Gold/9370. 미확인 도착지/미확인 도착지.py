"미확인 도착지"

import sys

case = int(sys.stdin.readline())


for _ in range(case):
    jum,sun,hubo = map(int,sys.stdin.readline().split())
    bum_st,bum_g,bum_h = map(int,sys.stdin.readline().split())
    bum_st -=1
    bum_g -=1
    bum_h -=1
    
    doro= [[] for i in range(jum)]
    
    for i in range(sun):
        inp_1,inp_2,inp_3= map(int,sys.stdin.readline().split())
        inp_1-=1
        inp_2-=1
        if((inp_1 == bum_g and inp_2 == bum_h) or (inp_2 == bum_g and inp_1 == bum_h)):
            doro[inp_1].append([inp_2,inp_3*2-1,i])
            doro[inp_2].append([inp_1,inp_3*2-1,i])
            bum_doro = i
        else:
            doro[inp_1].append([inp_2,inp_3*2,i])
            doro[inp_2].append([inp_1,inp_3*2,i])
    hubo_q = []
    for i in range(hubo):
        hubo_q.append(int(sys.stdin.readline())-1)
    hubo_q = sorted(hubo_q)
    q = [i for i in range(jum)]
    jum_li = [[-1] for i in range(jum)]
    
    minjum_index = bum_st
    minjum = 0
    
    jum_li[minjum_index] = [0]
    q.remove(minjum_index)

    while q:
        for i in range(len(doro[minjum_index])):
            if(jum_li[doro[minjum_index][i][0]][0] == -1 or jum_li[doro[minjum_index][i][0]][0] > jum_li[minjum_index][0]+doro[minjum_index][i][1]):
                jum_li[doro[minjum_index][i][0]][0] = jum_li[minjum_index][0]+doro[minjum_index][i][1]
        
        minjum = -1
        minjum_index = -1
        for i in range(len(q)):
            if(jum_li[q[i]][0] != -1 and (minjum == -1 or minjum > jum_li[q[i]][0])):
                minjum = jum_li[q[i]][0]
                minjum_index = q[i]
        if(minjum_index == -1):
            break

        q.remove(minjum_index)

    for i in range(len(hubo_q)):
        if(jum_li[hubo_q[i]][0] % 2 == 1 and jum_li[hubo_q[i]][0] != -1):
            print(hubo_q[i]+1,end=" ")

    print()