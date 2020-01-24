a=input()
k=''
for i in a:
    if i not in k:
          p=a.count(i)
          print(i,':',p)
          k+=i
