a = int(input())
li = []
c1 = 0
li2 = [0 for i in range(8001)]
for i in range(a):
    c = int(input())
    c1+=c
    li.append(c)
    li2[4000+c] += 1
li = sorted(li)
print(round(c1/len(li)))
print(li[len(li)//2])
hi=0
wi = 0
for i in range(len(li2)):
    if(li2[i] > hi):
        hi = li2[i]
        wi = i
        ss1=(i)-4000
li2[wi] = 0
hi2 = 0
for i in range(len(li2)):
    if(li2[i] > hi2):
        hi2 = li2[i]
        wi1 = i
        ss=(i)-4000
if(hi == hi2): print(ss)
else: print(ss1)
print(abs(li[0]-li[len(li)-1]))