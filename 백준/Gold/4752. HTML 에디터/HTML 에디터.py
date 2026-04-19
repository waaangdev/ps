from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write
while True:
    inp = input().strip()
    st,ed = int(inp.split()[0]),int(inp.split()[1])
    if(st+ed == -2):break
    text = inp[len(str(st))+len(str(ed))+2:]
    #print(text)

    tag = []
    text_index = 0
    is_tag = 0
    tagname = ""
    r = ""
    for i in range(len(text)):
        text_index = i
        
        if(text_index == st):
            for j in tag:
                r+= "<"+j+">"
        if(text_index == ed):
            for j in tag[::-1]:
                r+= "</"+j+">"
            break
        dum = text[i]
        if(is_tag):
            if(dum == ">"):
                is_tag = 0
                if(tagname[0] == '/'):
                    tag.pop()
                    if(text_index >= st):
                        r+="<"+tagname+">"
                else:
                    tag.append(tagname)
                    if(text_index >= st):
                        r+="<"+tagname+">"
            else:
                tagname+=dum
        else:
            if(dum == "<"):
                is_tag = 1
                tagname = ""
                continue
            if(text_index >= st):
                r+=dum
        #print(tag)
    print(r+"\n")