nome = input("Qual seu nome?")
dat_nas = input("Qual ano de nascimento?")
anoatual = input("Estamos em que ano?")

idade = float(anoatual) - float(dat_nas)
idade = int(idade)
print('Sua idade provavelmente é ' + str(idade) + '!')
