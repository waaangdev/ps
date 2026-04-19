import sys

w,h = map(int,input().split())
powli = [pow(2,i) for i in range(61)]
r = 0
idx = 1
queue = 0

def print2(*li):
    s = ""
    for i in li:
        s+=str(i)+" "
    s+="\n"
    sys.stdout.write(s)
    sys.stdout.flush()

sys.setrecursionlimit(61)

print = print2
input = sys.stdin.readline

def search(l,r,i):
    if(l+1 == r):
        return l
    dum = (l+r)//2
    print("?",i,dum)
    #queue += 1
    inp = input().strip()
    if(inp == "sky"):
        return search(l,dum,i)
    else:
        return search(dum,r,i)

dp = [h+1]*10000#얘보다 작은가?
left = [True]*10000
p = 0
rdum = 0
pdum = 0
pdum2 = p
pdum3 = 0
dp_left = w
run = True
q = [[i,0] for i in range(1,w+1)]
padd = 0

#f = open('./debug.txt', 'w')

while run:
    dumdum = 0
    for i in q:
        i=i[0]
        if(dp[i-1] > r):
            dum = r+powli[max(0,p)]
            if(dp[i-1] > dum):
                dumdum = 1
                #f.write(str(i)+" "+str(dum)+" "+str(dp_left)+" "+str(rdum)+" "+str(r)+" "+str(p)+" "+"\n")
                print("?",i,dum)
                inp = input().strip()
                if(inp == "sky"):
                    dp[i-1] = dum
                    if(pdum3 <= dp_left//500):
                        pdum3 += 1
                        pdum2 = p
                        pdum = p
                    else:
                        pdum2 -=1
                        r = rdum
                    p = pdum2
                    p = max(0,p)
                    #f.write("sky\n")
                else:
                    if(rdum < dum):
                        rdum = dum
                        idx = i
                    p=p+max(0,pdum-p-2)+1
                    #f.write("p "+str(p)+"\n")
                    pdum = p
                    pdum2 = p
                    pdum3 = 0
                    p = (min(60,p))

                    while(r+powli[p] > h and r != h):
                        #f.write("over"+"\n")

                        r = rdum
                        p -= 1#-20
                        p = max(0,p)
                        pdum = p
                        pdum2 = p
                        #lastp = 0
            else:
                if(p==0):
                    if(left[i-1]):
                        left[i-1]=False
                        dp_left-=1
        else:
            if(left[i-1]):
                left[i-1]=False
                dp_left-=1
        
        if(dp_left == 1):
            run=False
            break
    if(dumdum == 0):
        r = rdum
        p -= 1
        p = max(0,p)
        pdum3 = 0
        pdum2 = p

    q = [[i,dp[i-1]] for i in range(1,w+1)]
    q.sort(key=lambda x:x[1])
    q = q[::-1]



r = search(r,dp[idx-1],idx)


print("!",idx,r)
sys.stdout.flush()