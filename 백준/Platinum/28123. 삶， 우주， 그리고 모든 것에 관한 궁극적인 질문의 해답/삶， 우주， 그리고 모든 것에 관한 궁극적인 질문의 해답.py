# a = (999999999999999992-1)//3
# b = a-301029995663981193
# print(b)

# c = (999999999999999992 - 2 //10)+1
# # print(c-b)
# n = 999999999999999992 
# k = 301029995663981193 
# r = 0

# a = (n-k*3)
# print(a)

# a = (999999999999999992-1)//3
# b = a-301029995663981193
# print(b)

# c = (999999999999999992 - 2 //10)+1
# print(c-b)


#n,k,x = map(int,input().split())


def sol (n,k,x):
    if(n < 2):
        return 0
    elif(n < 12):
        return 1
    else:
        a = ((n-k*3)+1)
        if(x <= 4):
            a+=1
            if(x==1):
                a+=1

        return a
n,k,x = map(int,input().split())
print(sol(n,k,x))
# for i in range(1001):
#     n,k,x,dum,r = input().split()
#     if(sol(int(n),int(k),int(x)) != int(r)):
#         break
