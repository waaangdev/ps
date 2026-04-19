li = [*open(0)]
for i in li:
    a,b,c = sorted(list(map(int,i.split())))
    d,e = b-a-1,c-b-1
    print(max(d,e))