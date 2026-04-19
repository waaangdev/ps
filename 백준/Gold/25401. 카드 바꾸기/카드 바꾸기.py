#카드 바꾸기

li1 = [0]*2000002
li2 = [0]*4000002
li3 = [0]*4000002

a = int(input())
li = list(map(int,input().split()))
r = 0


max1 = 0
for i in li:
    li1[i+1000000] += 1
    max1 = max(li1[i+1000000],max1)

r = a-max1
#print(r)
for i in range(0,a):
    max1 = 0
    for j in range(0,a):
        if(j-i!=0):
            if((li[j]-li[i])%(j-i)==0):
                dum = ((li[j]-li[i])//(j-i))+1000000
                if(li3[dum]!=i):
                    li3[dum] = i
                    li2[dum] = 0
                li2[dum] += 1
                max1 = max(li2[dum],max1)
    r = min(r,a-max1-1)
print(r)