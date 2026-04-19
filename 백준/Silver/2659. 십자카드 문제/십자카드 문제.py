def sol(li):
    r = 10000
    for i in range(4):
        r = min(int(li),r)
        li = li[1:]+li[0]
    return (r)

n = sol(''.join(input().split()))
r = 0
#print(n)
for i in range(n):
    if(i > 1000):
        if(str(i).find('0')==-1):
            if(i == sol(str(i))):
                r+=1
                #print(i)
print(r+1)