n = int(input())
li = []
for _ in range(n):
    li.append(float(input()))
li.sort()
print('\n'.join(list(map(lambda x:"{:.3f}".format(x),li[:7]))))