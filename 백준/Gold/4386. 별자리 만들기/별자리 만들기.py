"별자리 만들기"

import sys
from collections import deque
import math

"최소 힙"
"입의 요소는 일차원 리스트로 구성 됨, 일차원 리스트의 첫 번째 요소를 기준으로 정렬 함"
class min_hip(): 
    def __init__(self,qwe = []):
        self.mhip = qwe
    def mappend(self,appyoso):
        #hip append
        app = appyoso
        self.mhip.append(app)
        hip_app_pos = len(self.mhip)-1
        while (hip_app_pos != 0):
            if(self.mhip[(hip_app_pos-1)//2][0] > app[0]):
                dum = self.mhip[(hip_app_pos-1)//2][:]
                self.mhip[(hip_app_pos-1)//2] = app[:]
                self.mhip[hip_app_pos] = dum
                hip_app_pos = (hip_app_pos-1)//2
            else:
                break
        return self.mhip
    def mpop(self):
        hip_pop = []
        hip_pop = self.mhip[0]
        self.mhip[0] = self.mhip[len(self.mhip)-1]
        del self.mhip[len(self.mhip)-1]
        hip_del_pos = 0
        hip = self.mhip
        
        while(hip_del_pos*2+1 < len(hip)):
            max_dum = hip[hip_del_pos*2+1][0]
            max_dum_i = hip_del_pos*2+1
            if(hip_del_pos*2+2 < len(hip)):
                if(max_dum > hip[hip_del_pos*2+2][0]):
                    max_dum = hip[hip_del_pos*2+2][0]
                    max_dum_i = hip_del_pos*2+2
            if(max_dum < hip[hip_del_pos][0]):
                hip_del_dum = hip[max_dum_i][:]
                hip[max_dum_i] = hip[hip_del_pos][:]
                hip[hip_del_pos][:] = hip_del_dum
                hip_del_pos = max_dum_i
            else:
                break
            
        return hip_pop

point_su= int(sys.stdin.readline())
point = [[0,0] for i in range(point_su)]
bang = [0 for i in range(point_su)]

for i in range(point_su):
    point[i] = list(map(float,sys.stdin.readline().split()))

npoint = 0
bang[0] = 1
bang_su = 1
hip = min_hip()
r = 0
while bang_su != point_su:
    for i in range(point_su):
        if(i != npoint):
            if(bang[i] == 0):
                hip.mappend([math.sqrt((point[npoint][0]-point[i][0])**2+(point[npoint][1]-point[i][1])**2),i])
    while 1:
        hip_pop = hip.mpop()
        if(bang[hip_pop[1]] == 0):
            bang[hip_pop[1]] = 1
            npoint = hip_pop[1]
            r+=hip_pop[0]
            bang_su += 1
            break
print(r)