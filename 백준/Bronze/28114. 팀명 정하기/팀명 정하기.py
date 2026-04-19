

a,b,c = input().split()
a1,b1,c1 = input().split()
a2,b2,c2 = input().split()

b = int(b)
b1 = int(b1)
b2 = int(b2)

h =[]

li = [str(b%100),str(b1%100),str(b2%100)]
li.sort()

print(li[0]+li[1]+li[2])

h.append([int(a),c])
h.append([int(a1),c1])
h.append([int(a2),c2])

h.sort()

print(h.pop()[1][0]+h.pop()[1][0]+h.pop()[1][0])