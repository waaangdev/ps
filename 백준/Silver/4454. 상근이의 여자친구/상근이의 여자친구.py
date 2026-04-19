import sys

inps = sys.stdin.readlines()


for i in inps:
    inp = list(map(float,i.split()))
    mt = inp[5]/inp[4]
    r = (mt)/inp[2]
    l = 0
    while (int(l*100)!=int(r*100)):
        v = (l+r)/2
        if(((inp[0]*(v**3)+inp[1]*(v**2)+inp[2]*(v)+(inp[3]))-mt) < 0):
            l = v
        else:
            r = v
    print(str(int(l*100))[:-2]+"."+str(int(l*100))[-2:])