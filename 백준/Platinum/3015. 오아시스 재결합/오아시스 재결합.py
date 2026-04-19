#오아시스 재결합
a = int(input())
li = [0 for i in range(a)]
for i in range(a):
    li[i] = int(input())
stack = []
r=0
dp = [0 for i in range(a)]
for i in range(a):
    for j in range(len(stack)):
        dum = stack[-1]
        if(dum[0] <= li[i]):
            r+=dp[dum[1]]+1
            if(dum[0] == li[i]):
                dp[i]+=dp[dum[1]]+1
            stack.pop()
        else:
            r+=1
            break
    stack.append([li[i],i])
print(r)