#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))   # Permite mostrar apenas interseções.
print(friends_set.difference(my_friends_set))   # Permite mostrar apenas diferentes.
print(friends_set.union(my_friends_set))   # Permite fazer uniões
