   try: 
      print(nome)     #Vai dar erro, pois nome não foi definido
   except:
      print('Nome não foi definido')
 print ('O programa continua, mesmo com o erro')
 
#outra forma... except identificado

   try: 
      print(nome)     #Vai dar erro, pois nome não foi definido
   except NameError as erro:     #Aqui eu indentifico, trato a excessão a classificação do erro (a propria IDE me retorna quando compilado o código) e salvo ele em uma variável, sendo que nesse caso o desenvolvedor já esperava pelo possível erro.
      print('O Erro é ', erro)
   except Exception as erro:     #Aqui informo que se por acaso houver outro erro não identificado ele passará por esse exception.
      print('Erro não identificado:  ', erro)
      
 print ('O programa continua, mesmo com o erro')
 

#outra forma...  uso do else

nome = 'Junior'
   try :
      print(nome)     #Não vai dar erro, o nome foi identificado
   except NameError as erro :    
      print('O Erro é ', erro)
   else :    #Se não houver nenhum erro, então ele pulará para o else
      print('Tudo certo!')
   
   
   

#outra forma...  uso do finally

nome = 'Junior'
   try :
      print(nome)     #Não vai dar erro, o nome foi identificado
   except NameError as erro :    
      print('O Erro é ', erro)
    finally:      #O finally sempre será executado, dando certo ou errado
		print('FIm desse bloco')
   
   
   
   
   
