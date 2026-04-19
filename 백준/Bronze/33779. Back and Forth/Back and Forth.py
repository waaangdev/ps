s=input()
r = "beep"
for i in range(len(s)):
    if(s[i]!=s[len(s)-1-i]):
        r = "boop"
print(r)