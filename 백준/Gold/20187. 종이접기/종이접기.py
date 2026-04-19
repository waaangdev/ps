k = int(input())
li =input().split()
h = int(input())

paper = [[h]]

for i in li[::-1]:
    if(i=='U'):
        lp = len(paper)
        for j in range(lp-1,-1,-1):
            paper.append([[2,3,0,1][k] for k in paper[j]])
    if(i=='D'):
        lp = len(paper)*2
        for j in range(0,lp,2):
            paper.insert(0,[[2,3,0,1][k] for k in paper[j]])
    if(i=='R'):
        lp = len(paper)
        for j in range(lp):
            paper[j] = ([[1,0,3,2][k] for k in paper[j]][::-1])+paper[j]
    if(i=='L'):
        lp = len(paper)
        for j in range(lp):
            paper[j] += ([[1,0,3,2][k] for k in paper[j]][::-1])
print('\n'.join([' '.join(list(map(str,i))) for i in paper]))