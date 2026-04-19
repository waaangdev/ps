n,m = map(int,input().split())
mapl = []
for _ in range(n):
    c = input()
    mapl.append([int(c[i]) for i in range(len(c))])
mapl[0][0] = 10
li = [[0,0]]

while 1:
    for i in range(len(li)):
        if(mapl[li[i][0]][li[i][1]] >= 10):
            for l in range(-1,2,2):
                if(li[i][1]+l >= 0 and li[i][1]+l < len(mapl[0])):
                    if(mapl[li[i][0]][li[i][1]+l] == 1):
                        mapl[li[i][0]][li[i][1]+l] = mapl[li[i][0]][li[i][1]]+1
                        li.append([li[i][0],li[i][1]+l])
            for l in range(-1,2,2):
                if(li[i][0]+l >= 0 and li[i][0]+l < len(mapl)):
                    if(mapl[li[i][0]+l][li[i][1]] == 1):
                        mapl[li[i][0]+l][li[i][1]] = mapl[li[i][0]][li[i][1]]+1
                        li.append([li[i][0]+l,li[i][1]])
            mapl[li[i][0]][li[i][1]] = 0

    if(mapl[len(mapl)-1][len(mapl[0])-1] >= 10):
        break
print(mapl[len(mapl)-1][len(mapl[0])-1]-9)