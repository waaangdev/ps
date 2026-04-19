T = int(input())
for i in range(T) :
    H, W, V = map(int, input().split())
    if H > V :
        print(str(V) + "01")
    else :
        pyogo = (V // H + 1)
        neungee = (V % H)
        if(neungee == 0): 
            neungee= H
            pyogo -= 1
        if pyogo > 9 :
                print(str(neungee) + str(pyogo))
        else :
                print(str(neungee) + "0" + str(pyogo))