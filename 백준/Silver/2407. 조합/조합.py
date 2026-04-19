from fractions import Fraction

a,b = map(int,input().split())
c = 1
for i in range(1,a+1):
    c *= i
d = 1
for i in range(1,b+1):
    d *= i
e = 1
for i in range(1,a-b+1):
    d *= i
    
print(Fraction(c, (d*e)))