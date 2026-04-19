import sys
a,d = map(int,input().split())

li2 = [[[1 for j in range(a+1)] for j in range(a+1)] for j in range(a+1)]
r = (a*(a-1)*(a-2))//6
for i in range(d):
    inp,inp2 = map(int,sys.stdin.readline().split())
    for j in range(1,a+1):
        if(j!=inp and j!= inp2):
            li = sorted([inp,inp2,j])
            r-=li2[li[0]][li[1]][li[2]]
            li2[li[0]][li[1]][li[2]] = 0
print(r)
    
    