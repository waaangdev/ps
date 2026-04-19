input()
if(sum(list(map(lambda x:{'O':1,'X':-1}[x],list(input()))))>=0):
    print("Yes")
else:
    print("No")