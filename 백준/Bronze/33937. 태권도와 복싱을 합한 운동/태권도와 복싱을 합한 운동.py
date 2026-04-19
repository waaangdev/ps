r =""
for I in range(2):
    a = input()
    r2=""
    dum=1
    dum2=0
    while dum2 < len(a):
          if(a[dum2] in list("aeiou")):
              dum=0
          elif dum==0:
              dum = -1
              break
          r2+=a[dum2]
          dum2+=1
    if dum != -1:
      r= "no such exercise"
      break
    r+=r2
print(r)