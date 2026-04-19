"보석 도둑"

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

                
            if((self.typ != "max" and self.mhip[(hip_app_pos-1)//2][0] > app[0]) or (self.typ == "max" and self.mhip[(hip_app_pos-1)//2][0] < app[0])):


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
                if((self.typ != "max" and max_dum > hip[hip_del_pos*2+2][0]) or (self.typ == "max" and max_dum < hip[hip_del_pos*2+2][0]) ):
                    max_dum = hip[hip_del_pos*2+2][0]
                    max_dum_i = hip_del_pos*2+2
            if((self.typ != "max" and max_dum < hip[hip_del_pos][0]) or (self.typ == "max" and max_dum > hip[hip_del_pos][0])):
                hip_del_dum = hip[max_dum_i][:]
                hip[max_dum_i] = hip[hip_del_pos][:]
                hip[hip_del_pos][:] = hip_del_dum
                hip_del_pos = max_dum_i
            else:
                break
            
        return hip_pop
    def mlen(self):
        return len(self.mhip)
        

n,k = map(int,sys.stdin.readline().split())

bosuk = [[0,0] for i in range(n)]

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    bosuk[i] = [a,b]
    
bag = [0 for i in range(k)]

for i in range(k):
    a = int(sys.stdin.readline())
    bag[i] = a
    
bag = sorted(bag)

bosuk = sorted(bosuk)

q= min_hip([],"max")
pointer = 0
r = 0


for i in range(k):
    while pointer != n:
        if(bosuk[pointer][0] > bag[i]):
            break
        q.mappend([bosuk[pointer][1]])
        pointer += 1
    if(q.mlen()):
        r += q.mpop()[0]
    
print(r)