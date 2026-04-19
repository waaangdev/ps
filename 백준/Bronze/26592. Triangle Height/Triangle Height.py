import sys
for i in range(int(input())):
    a,b=list(map(float,sys.stdin.readline().split()))
    print("The height of the triangle is {:.2f} units".format(2*a/b))