import sys

#ko_orange

# def sol(l,r,centerUP,lied):
#     dum = (l+r)//2
    
#     if(centerUP and not lied):
#         dum2 = (dum+r)//2
#         dum3 = (l+dum)//2
#         sys.stdout.write("? "+str(dum2)+"\n")
#         inp = input()
#         if(inp == "1"):
#             sol(dum2,r,True,lied)
#         else:
#             sys.stdout.write("? "+str(dum3)+"\n")
#             inp = input()
#             if(inp == "1"):
#                 sys.stdout.write("? "+str(dum)+"\n")
#                 inp = input()
#                 if(inp == "1"):
#                     sol(dum,dum2,False,lied)
#                 else:
#                     sol(dum3,dum,False,True)
#             else:
#                 sol(l,dum3,False,True)

#     else:
#         if(r-l < 2):
#             sys.stdout.write("! "+str(l)+"\n")
#             return
#         sys.stdout.write("? "+str(dum)+"\n")
#         inp = input()
#         if(inp == "0"):
#             sol(l,dum,False,lied)
#         else:
#             if(lied):
#                 sol(dum,r,False,lied)
#             else:
#                 sol(l,r,True,lied)
#                 # dum2 = (dum+r)//2
#                 # dum3 = (l+dum)//2
#                 # sys.stdout("?"+str(dum2)+"\n")
#                 # if(inp == "1"):
#                 #     sol(dum2,r,lied)


def query(num):
    sys.stdout.write("? "+str(num)+"\n")
    return int(input())

def sol(min_value,max_value,div_value,is_lied):

    center = (min_value+max_value)//2

    if(min_value +1== max_value):
        print('!',min_value)
        return

    
    if(is_lied):
        inp = query(center)
        if(inp == 0):
            sol(min_value,center,-1,is_lied)
        else:
            sol(center,max_value,-1,is_lied)

    else:
        if(div_value != -1):
            right = (center+max_value)//2
            left = (center+min_value)//2

            inp = query(right)
            if(inp == 0):
                if(min_value+1 == right):
                    print('!',min_value)
                    return

                inp = query(center)
                if(inp == 0):
                    sol(min_value,center,-1,True)
                else:
                    sol(center,right,-1,is_lied)
            else:
                sol(center,max_value,right,is_lied)
            return

        inp = query(center)
        if(inp == 0):
            sol(min_value,center,-1,is_lied)
        else:
            sol(min_value,max_value,center,is_lied)

cases = int(input())
for i in range(cases):
    sol(2100,2400,-1,False)

