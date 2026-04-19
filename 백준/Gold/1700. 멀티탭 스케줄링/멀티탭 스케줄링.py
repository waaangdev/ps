a,b= map(int,input().split())

li = list(map(int,input().split()))
li2 = [0 for i in range(b)]
li3 = [[0 for i in range(b)] for i in range(b)]

for i in range(b-1,-1,-1):
    li3[i] = [(j-i <= 0)*200 + (j-i > 0)*(j-i) for j in li2]
    li2[li[i]-1] = i

mlti = [0 for i in range(b)]
mlti_c = 0

r = 0

for i in range(b):
    if(mlti_c < a):
        if(mlti[li[i]-1] == 0):
            mlti[li[i]-1] = 1
            mlti_c += 1
    elif(mlti[li[i]-1] == 0):
        max_i = 0
        max_ = 0
        for j in range(b):
            if(li3[i][j] > max_ and mlti[j] == 1):
                max_ = li3[i][j]
                max_i = j
        mlti[max_i] = 0
        r+=1
        
        mlti[li[i]-1] = 1
print(r)