n=int(input())
if(n%10 == 6):
    print("Yes")
    print("0 1 0 "+"2 1 2 1 2 0 1 0 1 0 "*(n//10)+"2 1 2 ")
elif(n%10 == 1):
    print("Yes")
    print("0 "+"2 1 2 1 2 0 1 0 1 0 "*(n//10))
else:
    print("No")