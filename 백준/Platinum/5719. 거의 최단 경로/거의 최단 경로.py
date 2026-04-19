"거의 최단 경로"

import sys
from collections import deque

class min_hip(): 
    def __init__(self,qwe = [],typ = "min"):
        self.mhip = qwe
        self.typ = typ
    def mappend(self,appyoso):
        #hip append
        app = appyoso
        self.mhip.append(app)
        hip_app_pos = len(self.mhip)-1
        while (hip_app_pos != 0):
            if(self.typ == "max"):
                typ1 = self.mhip[(hip_app_pos-1)//2][0]
                self.mhip[(hip_app_pos-1)//2][0] = app[0]
                app[0] = typ1
                
            if(self.mhip[(hip_app_pos-1)//2][0] > app[0]):
                if(self.typ == "max"):
                    typ1 = self.mhip[(hip_app_pos-1)//2][0]
                    self.mhip[(hip_app_pos-1)//2][0] = app[0]
                    app[0] = typ1
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
            if(self.typ == "max"):
                typ1 = max_dum
                max_dum = hip[hip_del_pos][0]
                hip[hip_del_pos][0] = typ1
            if(max_dum < hip[hip_del_pos][0]):
                if(self.typ == "max"):
                    typ1 = max_dum
                    max_dum = hip[hip_del_pos][0]
                    hip[hip_del_pos][0] = typ1
                hip_del_dum = hip[max_dum_i][:]
                hip[max_dum_i] = hip[hip_del_pos][:]
                hip[hip_del_pos][:] = hip_del_dum
                hip_del_pos = max_dum_i
            else:
                break
            
        return hip_pop
    def mlen(self):
        return len(self.mhip)

def dijkstra(dway,dpoi_su,dst,dend):
    min_poi_i = st
    li = [-1 for i in range(dpoi_su)]
    lir = [deque([]) for i in range(dpoi_su)]
    li[st] = 0
    bang = dpoi_su-1
    bangli = [True for i in range(dpoi_su)]
    q = min_hip([])
    
    while bang:
        for i in range(dpoi_su):
            if(dway[min_poi_i][i] != -1 and bangli[i]):
                dum = li[min_poi_i]+dway[min_poi_i][i]
                if(dum < li[i] or li[i] == -1):
                    q.mappend([dum,i])
                    li[i] = dum
                    lir[i] = deque([])
                if(dum <= li[i]):
                    lir[i].append(min_poi_i)
        if(q.mlen() == 0):break
        while 1:
            if(q.mlen() == 0):break
            qpop = q.mpop()
            min_poi_i = qpop[1]
            if(bangli[min_poi_i]):
                break
        bangli[min_poi_i] = False
        if(min_poi_i == end): break
        bang -= 1
    return lir,li[end]
    
while 1:
    poi_su,way_su = map(int,sys.stdin.readline().split())
    if(poi_su == 0 and way_su == 0):break
    st,end = map(int,sys.stdin.readline().split())
    way = [[-1 for i in range(poi_su)] for i in range(poi_su)]
    
    for i in range(way_su):
        inp = list(map(int,sys.stdin.readline().split()))
        way[inp[0]][inp[1]] = inp[2]
    
    ptime = -1
    li,time = dijkstra(way,poi_su,st,end)
    q = deque([end])
    while q:
        qpop = q.popleft()
        for i in range(len(li[qpop])):
            qqpop = li[qpop].popleft()
            q.append(qqpop)
            way[qqpop][qpop] = -1
    
    li,time = dijkstra(way,poi_su,st,end)   
        
    print(time)