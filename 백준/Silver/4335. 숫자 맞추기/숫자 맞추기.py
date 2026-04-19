lst = [1 for i in range(11)]
while 1:
    n = int(input())
    if n == 0: break
    a = input()
    if a == "too high":
        for i in range(n, 11): lst[i] = 0
    elif a == "too low":
        for i in range(n+1): lst[i] = 0
    else:
        if lst[n] == 0: print("Stan is dishonest")
        else: print("Stan may be honest")
        lst = [1 for i in range(11)]