l= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
t=[ i for i in l if len(i)!=0]
print(t)
