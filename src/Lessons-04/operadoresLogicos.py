"""
Operadores Lógicos - aula 4

and, or, not
in e not in

"""

#(Verdadeiro E Verdadeiro) = Verdadeiro
#( verdadade e false) = false
#só vai retornar verdade se os dois forem verdade

#comparacao1 and comparacao2

a = 2
b = 3



if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')



#Not é bem usado em comparaçoes de valores vazios 

a = ''
b = 0

if not a:
    print('Por favor, preencha o valor de  A')


nome = 'Cassio Lcuaino da silva'

if 'vio' not in nome:
    print("Executei.")
else:
    print("Existe o texto.")