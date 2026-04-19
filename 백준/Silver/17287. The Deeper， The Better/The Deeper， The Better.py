a = input()
stack = []
sc = 0
r = 0
for i in a:
    if(i in list("({[")):
        sc += list("({[").index(i)+1
        stack.append(i)
    
    elif(i in list(")}]")):
        sc -= list(")}]").index(i)+1
        stack.pop()
    else:
        r = max(r,sc)
print(r)