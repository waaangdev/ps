n=0
m = 0
for i in range(4):
    n+=eval("-"+input().replace(" ","+"))
    m=max(m,n)
print(m)