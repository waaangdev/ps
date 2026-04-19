a=int(input())
b=int(input())
for i in " "*b:
    a-=int(eval(input().replace(" ","*")))
print(["No","Yes"][a==0])