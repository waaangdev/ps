b =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while 1:
    a = list(input())
    if (a == ['#']):
        break
    c = 0
    for i in a:
        if i in b:
            c +=1
    print(c)