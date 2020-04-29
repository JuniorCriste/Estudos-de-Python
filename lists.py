friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
new_friends = friends[:]  # new_friends = friends.copy()    OR   new_friends = list(friends)
print(friends)
print(new_friends)

# organziar lista -> friends.sort ()
# organiar lista ao contrario -> friends.sort(reverse=True)
# Remover ultima posição da lista -> friends.pop()
# Remover posição específica da lista -> friends.pop(2)
# Deletar posição específica da lista -> del friends[2]
# medir quantidade de itens da lista -> print(len(cars))
# Limpar uma lista -> friends.clear()
# Somar lista -> print(sum(cars))
# primeiro da lista por ordem -> print(min(friends))
# Ultimo da lista por ordem -> print(max(friends))
# Adicionar nome na lista -> friends.append('Nome')
# Adicionar nome na lista -> friends.append('Nome')
# Adicionar item na lista na lista -> friends.append('Alice')
# Adicionar um item na lista em um index específico ->friends.insert(1,'TerryG')          OU        friends[2]='Junior'
