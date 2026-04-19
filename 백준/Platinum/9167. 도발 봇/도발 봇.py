"도발 봇"

import sys

def gen(dum):
    global count
    if(dum in bang):
        bang[dum] = bang[dum]+1
    else:
        bang[dum] = 0
    if(dum == "taunt"):
        if(bang[dum]%len(sun[dum]) == 1):
            count += 1
    if(sun[dum][bang[dum]%len(sun[dum])][0] == '1'):
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "1"):
            ddddum = gen("sentence")
            ddddum = chr(ord(ddddum[0])-(ord('a')-ord('A'))) + ddddum[1:] 
            return ddddum
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "2"):
            ddddum1 = gen("taunt")
            ddddum = gen("sentence")
            ddddum = chr(ord(ddddum[0])-(ord('a')-ord('A'))) + ddddum[1:] 
            return ddddum1+" "+ddddum
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "3"):
            ddddum = gen("noun")+"!"
            ddddum = chr(ord(ddddum[0])-(ord('a')-ord('A'))) + ddddum[1:] 
            return ddddum
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "4"):
            ddddum = gen("sentence")
            ddddum = chr(ord(ddddum[0])-(ord('a')-ord('A'))) + ddddum[1:] 
            return ddddum
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "5"):
            return gen("past-rel")+" "+gen("noun-phrase")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "6"):
            return gen("present-rel")+" "+gen("noun-phrase")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "7"):
            return gen("past-rel")+" "+gen("article")+" "+gen("noun")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "8"):
            return gen("article")+" "+gen("modified-noun")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "9"):
            return gen("noun")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "10"):
            return gen("modifier") +" "+gen("noun")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "11"):
            return gen("adjective")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "12"):
            return gen("adverb")+" "+gen("adjective")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "13"):
            return 'your '+ gen("present-person")+" "+ gen("present-verb")
        if(sun[dum][bang[dum]%len(sun[dum])][1:] == "14"):
            return 'your '+ gen("past-person")+" "+ gen("past-verb")
        
    return sun[dum][bang[dum]%len(sun[dum])]

bang = {}
sun = {
    "taunt":["11","12","13","14"],
    "sentence":["15","16","17"],
    "noun-phrase":["18"],
    "modified-noun":["19" , "110"],
    "modifier":["111" , "112"],
    "present-rel":["113"],
    "past-rel":["114"],
    "present-person":['steed' , 'king' , 'first-born'],
    "past-person":['mother', 'father', 'grandmother', 'grandfather', 'godfather'],
    "noun":["hamster", "coconut", "duck", "herring", "newt", "peril", "chicken", "vole", 'parrot', 'mouse', 'twit' ],
    "present-verb":["is", "masquerades as"],
    "past-verb":["was","personified"],
    "article":["a"],
    "adjective":["silly", "wicked", "sordid", "naughty", "repulsive", "malodorous", "ill-tempered"],
    "adverb":["conspicuously", "categorically", "positively", "cruelly", "incontrovertibly"]

}

holy = "theholygrail"


while 1:
    try:
        inp =  sys.stdin.readline()
    except:
        break
    ddum = 0
    for i in range(len(inp)):
        if(inp[i] == holy[ddum] or inp[i] == chr(ord(holy[ddum])-(ord('a')-ord('A')))):
            ddum += 1
            if(ddum == len(holy)):
                break
    inp = inp.split()
    if(not inp):
        break
    
    print("Knight:",*inp,end = '\n')
    dddum = 0

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if(ord(inp[i][j]) >= ord("A") and ord(inp[i][j]) <= ord("z")):
                dddum += 1
                break

    i = 0
    while (i < (dddum+2)//3):
        if(ddum == len(holy)):
            print("Taunter: (A childish hand gesture).")
            i += 1
            ddum = 0
        else:
            count = 1
            qwe = gen("taunt")
            print("Taunter:",qwe+".")
            i += count
    print()