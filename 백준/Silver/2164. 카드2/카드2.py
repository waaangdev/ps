import collections
a = int(input())
li = [i+1 for i in range(a)]
li = collections.deque(li)
while 1:
    if(len(li) == 1):
        break
    del li[0]
    li.append(li.popleft())
print(li[0])