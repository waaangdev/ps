# #요세푸스 3

# #n,k = map(int,input().split())
# for k in range(1,20):
#     for n in range(1,20):
#         li = [1 for i in range(n)]
#         idx = 0
#         rl = 0
#         for i in range(n):
#             dum = 0
#             while 1:
#                 if(li[idx]):
#                     dum+=1
#                 if(dum==k):break
#                 idx+=1
#                 idx = idx%n

#             rl=(idx+1)
#             li[idx]=0
#         print(str(rl).ljust(2),end=' ')
#     print() 

# print()

# for k in range(1,20):
#     li = [0]*1000
#     for n in range(1,20):
#         if(n==1):
#             li[n] = 1
#         else:
#             li[n] = (li[n-1]+k-1)%(n)+1
#         print(str(li[n]).ljust(2),end=' ')
#     print() 

n,k = map(int,input().split())
his = 1
for n2 in range(2,n+1):
    his = (his+(k-1))%(n2)+1
print(his)