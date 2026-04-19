import sys
input()
ss = sys.stdin.readline().strip()
ud = [0,0]
r = 0
st = 0
for s in ss:
    if(s=='['):
        r += max(ud)
        ud = [1,1]
    elif(s==']'):
        r += 1
        ud = [0,0]
    elif(s=='2'):
        r+=1
        if(ud==[0,1]):
            r+=1
        ud = [0,1]
    elif(s=='5'):
        r+=1
        if(ud==[1,0]):
            r+=1
        ud = [1,0]
    st = 1
    
print(r)