#키로거
import sys
n = int(input())
for i in range(n):
    l = sys.stdin.readline().strip()
    li = [["",-1,1],["",0,-1]]
    idx = 0
    for j in l:
        if(j == '-'):
            if(idx!=0):
                li[idx][0] = ""
                li[li[idx][1]][2] = li[idx][2]
                li[li[idx][2]][1] = li[idx][1]
                idx = li[idx][1]
        elif(j == '<'):
            if(li[idx][1]!=-1):idx = li[idx][1]
        elif(j == '>'):
            if(li[idx][2]!=1):idx = li[idx][2]
        else:
            li.append([j,idx,li[idx][2]])
            li[li[idx][2]][1] = len(li)-1
            li[idx][2] = len(li)-1
            idx = len(li)-1
        
        # idx2 = 0
        # for j in range(len(li)):
        #     print(li[idx2][0],end="")
        #     if(idx2==idx):print("_",end ="")
        #     idx2 = li[idx2][2]
        #     if(idx2 == -1):
        #         break
        # print()
    idx = 0
    for j in range(len(li)):
        print(li[idx][0],end="")
        idx = li[idx][2]
        if(idx == -1):
            break
    print()