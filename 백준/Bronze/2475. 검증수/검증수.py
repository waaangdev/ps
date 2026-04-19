li = list(map(int,input().split()))
a = 0
for i in range(5):
    a+= li[i]**2
print(a%10)