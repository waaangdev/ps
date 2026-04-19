import sys
a = input()
b = a[0]
c = 0
for i in range(len(a)):
    if(a[c] == b):
        c+=1
    else:
        break
print(c)
