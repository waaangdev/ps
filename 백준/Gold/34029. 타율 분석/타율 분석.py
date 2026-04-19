import math

def C(n,k):
    return math.factorial(n)/math.factorial(n-k)/math.factorial(k)

a,b = input().split()
a=float(a)
b=int(b)
dum = 0
for i in range(b+1):
    dum += C(b,i)*(a**i)*((1-a)**(b-i))
    if(dum >= 0.05):
        print(i)
        break