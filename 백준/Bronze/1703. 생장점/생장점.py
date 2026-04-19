import sys
while(1):
    a=list(map(int,sys.stdin.readline().split()))
    if(a==[0]):break 
    b=1
    for I in range(1,len(a),2):
        b*=a[I]
        b-=a[I+1]
    print(b)