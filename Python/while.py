numeros = []
i=0
quantidade = float(input('Quantos números quer somar?'))

while i < quantidade:
    numeros.insert(i, int(input('Digite o' + str(i + 1) + 'º numero para a soma')))
    i=i+1

soma = int(sum(numeros))
print ('Números digitados: ' + str(numeros))
print ('A soma dos números é ' + str(soma) + '!')
