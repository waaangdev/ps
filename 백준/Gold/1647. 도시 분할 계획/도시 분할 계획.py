"도시 분할 계획"

import sys
from collections import deque


point_su,way_su = map(int,sys.stdin.readline().split())

point = [0]*point_su
way = [[] for i in range(point_su)]

for i in range(way_su):
    inp = list(map(int,sys.stdin.readline().split()))
    inp[0] -=1
    inp[1] -=1
    way[inp[0]].append([inp[1],inp[2]]) 
    way[inp[1]].append([inp[0],inp[2]]) 

r = 0
point[0] = 1
hip = []
pos = 0 #최근업뎃위치
r1 = 1 #방문한노드개수
mmaxx = 0


while (r1 != point_su):
    #print("app")
    for i in range(len(way[pos])):
        #hip append
        app = (way[pos][i][1],way[pos][i][0])
        hip.append(app)
        hip_app_pos = len(hip)-1
        while (hip_app_pos != 0):
            if(hip[(hip_app_pos-1)//2][0] > app[0]):
                dum = hip[(hip_app_pos-1)//2]
                hip[(hip_app_pos-1)//2] = app
                hip[hip_app_pos] = dum
                hip_app_pos = (hip_app_pos-1)//2
            else:
                break
            #print("----",point,hip,r,r1)
    #print("--",point,hip,r,r1)
    

    #print("pop")
    while 1:
        hip_pop = []

        #hip pop
        hip_pop = hip[0]
        hip[0] = hip[len(hip)-1]
        del hip[len(hip)-1]
        hip_del_pos = 0

        while(hip_del_pos*2+1 < len(hip)):
            max_dum = hip[hip_del_pos*2+1][0]
            max_dum_i = hip_del_pos*2+1
            if(hip_del_pos*2+2 < len(hip)):
                if(max_dum > hip[hip_del_pos*2+2][0]):
                    max_dum = hip[hip_del_pos*2+2][0]
                    max_dum_i = hip_del_pos*2+2
            if(max_dum < hip[hip_del_pos][0]):
                hip_del_dum = hip[max_dum_i]
                hip[max_dum_i] = hip[hip_del_pos]
                hip[hip_del_pos] = hip_del_dum
                hip_del_pos = max_dum_i
            else:
                break



        if(point[hip_pop[1]] == 0):
            point[hip_pop[1]] = 1
            pos = hip_pop[1]
            r += hip_pop[0]
            r1+=1
            mmaxx = max(hip_pop[0],mmaxx)

            break
    #print("--",point,hip,r,r1)
print(r-mmaxx)