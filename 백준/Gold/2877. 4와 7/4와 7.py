i = int(input())
r=bin(i+1)[3:]
r=r.replace('0','4')
r=r.replace('1','7')
print(r)