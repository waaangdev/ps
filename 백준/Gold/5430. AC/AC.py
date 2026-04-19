from collections import deque
import sys
a = int(input())
for _ in range(a):
    b = 0
    od = sys.stdin.readline().strip()
    q = input()
    li = sys.stdin.readline().strip().split(',')
    if(q == '0'):
        li = deque([])
        lin = 0
    else:
        li[0] = li[0][1:]
        li[-1] = li[-1][0:-1]
        li = [int(i) for i in li]
        li = deque(li)
        lin = len(li)
    for i in range(len(od)):
        odd = od[i]
        if(odd == 'R'):
            b = -b + 1
        if(odd == 'D'):
            if(lin != 0):
                if(b == 0):
                    li.popleft()
                else:
                    li.pop()
                lin -=1
            else:
              print("error")
              lin =-1
              break
    if(lin != -1):
        if(b == 1):
            li = list(reversed(list(li)))
        else:
           li =list(li)
        print("[",end = "")
        if(lin != 0):
            print(str(li[0]),end = "")
        for i in range(lin-1):
          print(","+str(li[i+1]),end = "")
        print("]")