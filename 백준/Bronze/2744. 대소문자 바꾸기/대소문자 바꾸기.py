inp = input()
for i in range(len(inp)):
    if(ord(inp[i]) >= ord('a')):
        print(chr(ord(inp[i])-(ord('a')-ord("A"))),end = '')
    else:
        print(chr(ord(inp[i])+(ord('a')-ord("A"))),end = '')