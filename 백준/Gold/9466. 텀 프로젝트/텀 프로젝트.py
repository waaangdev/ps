"텀프로젝트.미해결"

import sys

case = int(sys.stdin.readline())

for _ in range(case):
    
    """
    
    li1 : 각 학생들이 어느 학생을 팀으로 선택했는지 주어지는 리스트
    r : 팀이 되지 않은 사람의 수

    li2 : 몆 번째로 방문했는지
    
    """
    
    lenli1 = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))
    li1bang = [False]*(lenli1+1)
    
    li1 = {}

    for i in range(lenli1):
        li1[i] = li[i]


    r = 0
    sib = 0
    
    for i in range(lenli1):
        pointer = i


        if(not li1bang[pointer]):
            li1bang[pointer] = True
            li2 = [pointer]

            for j in range(lenli1):
                pointer = li1[pointer]-1
                if(li1bang[pointer]):
                    if(pointer in set(li2)):
                        r += len(li2)-li2.index(pointer)
                    break
                li2.append(pointer)
                li1bang[pointer] = True
    print(lenli1-r)
            