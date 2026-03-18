for i in range(int(input())):
    n = int(input())
    if(0<n <= 2):
        n-=1
    
    n+=max(0,n-3)
    if(n%2 == 0):
        print("1 0")
    else:
        print("0 1")
    