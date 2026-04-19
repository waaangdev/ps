a,b = map(int,input().split())
s = ['?' for i in range(a)]
p = 0
w = 0
for i in range(b):
    c,d = input().split()
    p += int(c)
    if(s[p%a] == '?' or s[p%a] == d):
        s[p%a] = d
    else:
        w = 1
h=[]
for i in range(len(s)):
    if(s[i] in h and s[i] != '?'):
        w = 1
        break
    h.append(s[i])
if(w == 0):
    for i in range(len(s)):
        print(s[(p-i)%a],end = '')
else: print('!')