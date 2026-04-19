n = 10
li = [0 for i in range(101)]
r = 0
for _ in range(n):
    num = (int(input())//10)
    r+=num
    li[num] += 1
print(r)
print(li.index(max(li))*10)