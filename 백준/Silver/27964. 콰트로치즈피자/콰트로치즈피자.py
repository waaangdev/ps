e = int(input())
li = input().split()
li2 =  []
r = "sad"
for i in li:
    if(i[-6:] == "Cheese"):
        if(not i in li2):
            li2.append(i)
    if(len(li2) == 4):
        r = "yummy"
        break
print(r)