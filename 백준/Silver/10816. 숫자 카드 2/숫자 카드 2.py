input()
li2 = list(map(int,input().split()))
li = {}
for i in li2:
    if(i in li):li[i] += 1
    else:li[i] = 1
input()
li2 = list(map(int,input().split()))
for i in li2:
    if(i in li):print(li[i],end = ' ')
    else:print(0,end = ' ')