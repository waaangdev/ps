li = list(map(int,input().split()))
li.sort()
dum= [li[i+1]-li[i] for i in range(2)]
if(dum[0]< dum[1]):
    print(li[1]+dum[0])
elif(dum[0]>dum[1]):
    print(li[0]+dum[1])
else:
    print(li[2]+dum[1])

