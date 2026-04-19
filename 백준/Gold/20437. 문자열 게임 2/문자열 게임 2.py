def sol():
    word = input()
    inpk = int(input())
    minr = -1
    maxr = -1
    abc = "qwertyuiopasdfghjklzxcvbnm"
    for i in abc:
        #print(i)
        p1,p2 = 0,0
        kin = 0
        while(1):
            while(p2 != len(word)):
                if(word[p2]==i): 
                    kin+=1
                    if(kin == inpk):
                        break
                p2+=1
            if(kin != inpk):break

            while(p1 != len(word)):
                if(word[p1]==i): 

                    if(minr==-1): minr = p2-p1+1
                    minr = min(p2-p1+1,minr)
                    maxr = max(p2-p1+1,maxr)

                    kin-=1
                    p2+=1
                    p1+=1
                    break
                p1+=1
        #print(maxr)
    if(minr+maxr == -2):
        print(-1)
    else:
        print(minr,maxr)



t = int(input())
for i in range(t):
    sol()

