while 1:
    a,b,c = sorted(list(map(int,input().split())))
    if(c==0):break
    print(["right","wrong"][a**2+b**2!=c**2])