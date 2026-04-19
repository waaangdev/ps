
import sys
from collections import deque


a = int(sys.stdin.readline())
for i in range(a):
    c,d = map(int,sys.stdin.readline().split())
    if(c < 159):
        if(c < 146):
            if(c <= 140):
                print(6)
            else:
                print(5)
        else:
            print(4)
    else:
        bmi = d/((c/100)*(c/100))
        if(c < 161):
            if(bmi >= 16 and bmi< 35):
                print(3)
            else:
                print(4)
            
        else:
            if(c < 204):
                if(bmi >= 20 and bmi< 25):
                    print(1)
                elif((bmi >= 18.5 and bmi< 20) or (bmi >= 25.0 and bmi< 30)):
                    print(2)
                elif((bmi >= 16 and bmi< 18.5) or (bmi >= 30 and bmi< 35)):
                    print(3)
                else:
                    print(4)
            else:
                print(4)
