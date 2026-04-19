import sys
n,m=list(map(int,sys.stdin.readline().split()))
li = []
for i in range(m):
    li.append(list(map(int,sys.stdin.readline().split())))
mins = min([i[1]-i[0]+1 for i in li])
# for i in range(m):
#     li[i] = [li[i][1]-mins,li[i][1]]
# li = sorted(li,key=lambda x:x[0])
li = [i%mins+1 for i in range(n)]
print(*li)