l = input()
if(len(l) < 2):
    print('CE')
elif(l=='""' or (l[0]!='"' or l[-1]!='"')):
    print('CE')
else:
    print(l[1:-1])