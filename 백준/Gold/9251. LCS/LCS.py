a = input()
b = input()

m = [[0 for i in range(len(b))] for j in range(len(a))]

lcs = 0

for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j]):
            if(i == 0 or j == 0):
                m[i][j] = 1
            else:
                m[i][j] = m[i-1][j-1]+1
                
            
            if(lcs < m[i][j]): lcs = m[i][j] 
        else:
            m[i][j] = max(m[i][j-1],m[i-1][j])

print(lcs)