a,b = map(int,input().split())
li =[]
li2 =[0 for i in range(b)]
c= 360/b
for i in range(a):
    dum = float(input())
    li.append([dum%c,int(dum//c)])
    li2[int(dum//c)] +=1
li.sort(key=lambda x:x[0])
r = max(li2)-min(li2)
dum = -1
for i in range(a):
    #print(li)
    dum2 = li[0][0]
    li2[li[0][1]] -=1
    if(li[0][1] == 0):
        li2[b-1] +=1
    else:
        li2[li[0][1]-1] +=1
    del li[0]
    if(dum != dum2):
        r = min(max(li2)-min(li2),r)
        #print(li2)
    dum = dum2
print(r)