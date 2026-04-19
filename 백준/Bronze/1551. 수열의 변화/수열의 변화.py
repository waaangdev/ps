n,k=list(map(int,input().split()))
li=list(map(int,input().split(",")))
for I in range(k):
    li=[li[i+1]-li[i] for i in range(n-I-1)]
print(",".join(list(map(str,li))))