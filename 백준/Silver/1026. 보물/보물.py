input()
li1 = list(sorted(list(map(int,input().split()))))
li2 = list(sorted(list(map(int,input().split()))))
li2  = list(reversed(li2))
r=0
for i in range(len(li2)):
    r+= li1[i] * li2[i]
print(r)
                 