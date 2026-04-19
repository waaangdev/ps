a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
li = [[b[i],c[i]] for i in range(a)]
li.sort()
li = li[::-1]
#print(li)
x = 0
t = 0
for i in range(a):
    t += abs(li[i][0]-x)
    x = li[i][0]
    t = max(t,li[i][1])
    #print(t)

t+=x
print(t)