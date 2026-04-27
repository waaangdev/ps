li = [input(),input(),input()]
d = 0
for i in range(3):
    if(li[i] not in ["FizzBuzz","Fizz","Buzz"]):
        d=int(li[i])
    d+=1
r = ''
if(d%3==0):
    r+="Fizz"
if(d%5==0):
    r+='Buzz'
if(r==''):
    r=int(d)
print(r)