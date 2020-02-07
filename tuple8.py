t=(2,34,54,34,34,556,6)
a=[]
for i in t:
      if t.count(i)>1:
          if i not in a:
             a.append(i)
print(a)
