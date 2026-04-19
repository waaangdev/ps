import sys
for i in range(int(input())):
    d1,d2=0,0
    a,b=list(map(int,sys.stdin.readline().split()))
    d1 = a/b
    a,b=list(map(int,sys.stdin.readline().split()))
    d2 = (3.141592*a)**2/b
    print(["Whole pizza","Slice of pizza"][d1>d2])