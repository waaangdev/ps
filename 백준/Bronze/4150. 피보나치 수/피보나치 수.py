a,b =1,1
for i in range(int(input())-1):
    a,b = b,a+b
print(a)