idade = float(input('Digite sua idade'))
    
if idade < 16:
    print ('Não tem idade para votar!')
elif idade >= 16 and idade < 18 or idade >= 70:
    print ('Voto é opcional!')
else:
    print ('Voto obrigatório!')
    
    
