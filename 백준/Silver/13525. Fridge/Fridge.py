import math
inp = input()
li = [0]*10
for i in range(10):
    li[i] = inp.count(str(i))
r= ""
br = 1
while (br):
    mins = len(inp)
    mini=0
    for i in range(10): 
        if((i!=0 or r!="")):
            if(li[i] < mins):
                mins = li[i]
                mini = i
            if(li[i]==0):
                r+=str(i)
                br = 0
                break
    if(br == 1):
        r+=str(mini)
        li[mini]-=1
print(r)