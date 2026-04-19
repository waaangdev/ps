a = int(input())
li = []
li2 = [[] for i in range(201)]
for i in range(a):
    li.append(input().split())
for j in range(len(li)):
    li2[int(li[j][0])].append(li[j])
for j in range(len(li2)):
    for i in range(len(li2[j])):
        print(li2[j][i][0],li2[j][i][1])