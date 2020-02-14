l=[1,4,5,65,(2,4)]
c=0
for i in l:
    if type(i)!=tuple :
         c+=1
    else:
           break
print(c)
