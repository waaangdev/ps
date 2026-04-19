a = int(input())

def recursion(s, l, r):
    if l >= r: return 1,1
    elif s[l] != s[r]: return 0,1
    else:
        q,w = recursion(s, l+1, r-1)
        return q,w+1

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(a):
    c = input()
    q,w = isPalindrome(c)
    print(q,w)
