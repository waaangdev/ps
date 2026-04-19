for i in range(int(input())):
    a,b,c = input().split()
    a=float('0'+a)
    b=float('0'+b)
    c=float('0'+c)
    print("$"+str("{:.2f}".format(a*b*c,2)))