n = 5
r = 0
for i in range(n):
    m = input()
    if(m.find("FBI")!= -1):
        print(i+1,end=" ")
        r= 1
if(r==0):
    print("HE GOT AWAY!")