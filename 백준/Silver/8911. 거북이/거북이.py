a = int(input())
angle = [[0,-1],[-1,0],[0,+1],[+1,0]]
for _ in range(a):
    li = input()
    pl = [0,0]
    pla = 0
    xs = 0
    xd = 0
    ys = 0
    yd = 0
    for i in range(len(li)):
        if(li[i] == 'F'):
            pl[0] += angle[pla%4][0]
            pl[1] += angle[pla%4][1]
        if(li[i] == 'B'):
            pl[0] -= angle[pla%4][0]
            pl[1] -= angle[pla%4][1]
        if(li[i] == 'L'):
            pla+=1
        if(li[i] == 'R'):
            pla-=1
        xs = min(xs,pl[0])
        xd = max(xd,pl[0])
        ys = min(ys,pl[1])
        yd = max(yd,pl[1])
    print(abs(xs-xd)*abs(ys-yd))