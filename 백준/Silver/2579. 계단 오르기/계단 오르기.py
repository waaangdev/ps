
a = int(input())
li = [int(input()) for _ in range(a)]
li2 = [[-1,-1] for _ in range(a)]
def q(asd,asd2):
    max_ = 0
    if(li2[asd][asd2] != -1):
        return li2[asd][asd2]
    
    if(asd >= 2):
        max_ = q(asd-2,0)
    if(asd2 != 1):
        if(asd >= 1):
            max_ = max(max_,q(asd-1,asd2+1))
    max_+=li[asd]
    li2[asd][asd2] = max_
    return max_
print(q(a-1,0))