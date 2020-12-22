'''''

Formatando valores com modificadores

:s - texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float) 
:.(NUMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> OU < OU ^) (quantidade )(Tipo - s d ou f)

> - Esquerda 
< - direita 
^ -  CENTRO

'''''
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 1150
print(f'{num_3:0^10}')


nome = 'cassio luciano da silva'
#função len conta a quantidade de caracteres
print(len('###############'))

print (f'{nome:#^50}')




#função format

nome = 'Cassio luciano da silvas'
nome_formatado = '{:@>60}'.format(nome)
print(nome_formatado)


# variaveis nomeadas
nome = 'Cassio luciano da silvas'
nome_formatado = '{n}{n}{n}{n}{n}{n}{n}{n}{n}{n}'.format(n = nome)
print(nome_formatado)

# indice
nome = 'Cassio'
sobrenome = 'Luciano'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome,sobrenome)
print(nome_formatado)


#ljust =  Vai completar meu nome até chegar em 30 caracteres

nome = 'Cassio luciano da silva'
nome = nome.ljust(30, '%')
print(nome)



nome = 'casSio luciaNo da silva'

print(nome.lower()) #imprime tudo maisculo 
print(nome.upper()) #imprime tudo minusculo
print(nome.title()) #Primeira letra maiscula