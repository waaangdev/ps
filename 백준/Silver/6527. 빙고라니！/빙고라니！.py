import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

lines = [*open(0)]
inp = ""
for i in lines:
    inp+=i
inp += " asd"
inp = inp.split("BULLSHIT")[:-1]
r = 0
for i in inp:
    i = list(i)
    for j in range(len(i)):
        if(i[j] not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"):
            i[j] = " "
        else:
            i[j] = i[j].lower()
    i = "".join(i)
    #print(i)
    r += len(set(i.split()))
    #print(len(set(i.split())))

#print(len(inp),r)
r2 = len(inp)
for i in range(1,r):
    if(r2 %i==0 and r%i==0):
        r2//=i
        r//=i
print(F"{r} / {r2}")