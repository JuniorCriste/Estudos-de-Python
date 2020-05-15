minha_lista = [1,5,-3,7,2]

minha_lista.sort() # organiza e modifica a lista em ordem crescente
print (minha_lista)


--------------------------

minha_lista = [1,5,-3,7,2]

minha_lista.reverse() # organiza e modifica a lista em ordem reversa a original, de trás para frente
print (minha_lista)


--------------------------

minha_lista = [1,5,-3,7,2]

print(sorted(minha_lista))  # organiza a lista em ordem crescente assim como o sort(), porém não modifica, não fica atribuído. Após isso a lista volta ao valor original. 


# print(sorted(minha_lista, key = abs))  Imprime em ordem crescente, porém ignora a lógica de positivo ou negativo.
