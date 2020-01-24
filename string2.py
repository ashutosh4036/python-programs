a=input().split()
k=[]
for i in a: 
    if i not in k:
        k=a.count(k)
        print(i,':',k)  
