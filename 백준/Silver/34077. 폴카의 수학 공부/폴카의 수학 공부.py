

import sys

a = int(input())
for i in range(a):
    sys.stdin.readline().strip()
    li = sys.stdin.readline().strip()
    if(li.find('-') ==-1):
        print("YES")
    else:
        li = [li[:li.find('-')]]+[li[li.find('-')+2:]]
        #print(li)
        if(len(li[1])!=0 and li[1].count('0') != len(li[1])//2):
            print("NO")
        else:
            print("YES")

#0-3+3