import math
while(1):
    n=int(input())
    if(n==-1):break
    r = 2
    for i in range(2,n):
        r*=i
    print(f"N={n}:\n{r}")