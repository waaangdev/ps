import sys
input()
li=sorted(list(map(int,sys.stdin.readline().split())))
r = 0
for i in range(1,len(li)):
    r+=(li[i]-li[i-1])*(i)*(len(li)-i)
print(r*2)