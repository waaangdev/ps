import sys
a = list(map(int,sys.stdin.readline().split()))
print(sum([i//3 for i in a])+max([i%3 for i in a])-(sum([(i%3 == 2)*100+(i%3 == 0)*1 for i in a]) == 102)*1)