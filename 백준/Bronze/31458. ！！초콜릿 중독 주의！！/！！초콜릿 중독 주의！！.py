n = int(input())
for _ in range(n):
    s = input()
    num = 0
    if(s.find('1')!=-1):
        num = 1
    s = s.replace('1',' ').replace('0',' ')
    s = [s.find(' '),len(s)-s.find(' ')-1]
    #print(s)
    if((s[1]) != 0):
        num=1
    print((num+s[0])%2)