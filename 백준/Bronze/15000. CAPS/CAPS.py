l=input()
print(''.join([chr(ord(i)-(ord('a')-ord('A'))) for i in l]))