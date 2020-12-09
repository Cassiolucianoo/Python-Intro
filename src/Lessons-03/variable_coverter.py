"""
convertendo variavel

"""

nome = input("Qual o seu nome ? ")
idade = input ("qual a sua idade ? ")

#pegando a variavel que inicia como string no input e convertendo ela para int 
#a entrada do input é sempre texto então a subtração pode dar erro sem converter 
ano_nascimento = 2021-int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')

print()
input("Aperte qualquer tecla e finalize")

