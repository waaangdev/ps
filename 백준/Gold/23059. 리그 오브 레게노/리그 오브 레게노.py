"리그 오브 레게노"

import sys
from collections import deque


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
    def mlen(self):
        return len(self.mhip)
    

way_su = int(sys.stdin.readline())
r = []
li = set([])
dic = {}
way2 = []

for i in range(way_su):
    dum = sys.stdin.readline().split()
    li.add(dum[0])
    li.add(dum[1])
    way2.append(dum)
li = list(li)
li.sort()

point_su = len(li)

for i in range(point_su):
    dic[li[i]] = i

way = [[] for i in range(point_su)]
point = [0 for i in range(point_su)]

for i in range(len(way2)):
    way[dic[way2[i][0]]].append(dic[way2[i][1]])
    point[dic[way2[i][1]]] += 1
    
#print(li,dic,way)
    
q = min_hip()
bang = [0 for i in range(point_su)]

r1 = 0

for i in range(point_su):
    if(point[i] == 0):
        q.mappend([i])
        bang[i] = 1
        r1 += 1


while q.mlen() != 0:
    lenq = q.mlen()
    li2 = []
    for _ in range(lenq):
        qpop = q.mpop()[0]
        r.append(li[qpop])

        for i in range(len(way[qpop])):
            point[way[qpop][i]] -= 1
            if(bang[way[qpop][i]] == 0 and point[way[qpop][i]] == 0):
                bang[way[qpop][i]] = 1
                li2.append([way[qpop][i]])
                r1 += 1

    for i in range(len(li2)):
        q.mappend(li2[i])

if(r1 == point_su):
    for i in range(point_su):
        print(r[i])
else:
    print(-1)