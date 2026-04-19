n1,r1,c1 = map(int,input().split())
cnt = 0
m = [[0 for i in range(n1)] for i in range(n1)]
def a(n,r,c):
    if(n == 1):
        global cnt
        if(r == c1 and c == r1):
            print(cnt)
        cnt +=1
    else:
        if(r1 < c+n//2 and c1 < r+n//2):
            a(n//2,r,c)
            cnt += pow(n//2,2)*3
        elif(r1 < c+n//2 and c1 >= r+n//2):
            cnt += pow(n//2,2)*1
            a(n//2,r+n//2,c)
            cnt += pow(n//2,2)*2
        elif(r1 >= c+n//2 and c1 < r+n//2):
            cnt += pow(n//2,2)*2
            a(n//2,r,c+n//2)
            cnt += pow(n//2,2)*1
        else:
            cnt += pow(n//2,2)*3
            a(n//2,r+n//2,c+n//2)
a(pow(2,n1),0,0)