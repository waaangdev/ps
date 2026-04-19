a = input()
li = []
li2 =['0','1','2','3','4','5','6','7','8','9']
c = 0
for i in a:
    if (i in li):
        li.remove(i)
    elif(i == '6' and '9' in li):
        li.remove('9')
    elif(i == '9' and '6' in li):
        li.remove('6')
    else:
        li = li+li2
        li.remove(i)
        c +=1
print(c)