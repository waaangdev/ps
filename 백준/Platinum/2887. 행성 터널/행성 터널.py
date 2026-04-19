import sys

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

poi_su = int(sys.stdin.readline())
poi = [[] for i in range(poi_su)]
way = [[] for i in range(poi_su)]

for i in range(poi_su):
    poi[i] = list(map(int,sys.stdin.readline().split()))+[i]

for i in range(3):
    poi.sort(key = lambda x : (x[i]))
    for j in range(poi_su):
        for k in range(-1,2,2):
            if(j+k >= 0 and j+k != poi_su):
                way[poi[j][3]].append([abs(poi[j][i]-poi[j+k][i]),poi[j+k][3]])
hip = min_hip()
bang = [True]*poi_su
bang[0] = False
bang_su = 1
r = 0
for i in range(len(way[0])):
    hip.mappend(way[0][i])
while (bang_su != poi_su):
    hippop =  hip.mpop()
    if(bang[hippop[1]]):
        r+=hippop[0]
        bang_su += 1
        bang[hippop[1]] = False
        for i in range(len(way[hippop[1]])):
            hip.mappend(way[hippop[1]][i])
            
print(r)
    
    