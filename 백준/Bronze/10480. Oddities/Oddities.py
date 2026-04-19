n=int(input())
print('\n'.join([(lambda x:x+" is "+['even','odd'][int(x)%2])(input()) for i in range(n)]))