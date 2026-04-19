s=input()+'--'
if(s[1]=='0'):
    if(s[3]=='0'):
        print(20)
    else:
        print(10+int(s[2]))
else:
    if(s[2]=='0'):

        print(10+int(s[0]))

    else:

        print(int(s[0])+int(s[1]))