a = int(input())
min = 1
max = a+1
while 1:
    print("?",(min+max)//2)
    b = input()
    if(b == '-1'):
        min = (min+max)//2
    elif (b == '1'):
        max = (min+max)//2
    else:
        print("=",(min+max)//2)
        break