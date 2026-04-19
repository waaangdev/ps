a,b = input().split()
li = [0]*27
if(len(a) > len(b) or (len(a)==len(b) and a>b)):
    a,b=b,a
a2=a+'{'*(len(b)-len(a))
for i in a2:
    li[ord(i)-ord('a')]+=1
for i in b:
    li[ord(i)-ord('a')]-=1
r = sum(map(abs,li))
if(a==b):
    print(f"{a} is identical to {b}")
elif(r==0):
    print(f"{a} is an anagram of {b}")
elif(r==2):
    print(f"{a} is almost an anagram of {b}")
else:
    print(f"{a} is nothing like {b}")
    