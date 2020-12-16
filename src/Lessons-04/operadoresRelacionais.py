"""

Operadores logicos

== igualdade > maio que
>= maior que ou igual a
< menor que
<= menor que oou igual a
!= diferente

"""

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade')

#Será que pode pegar imprestimo
idade_limite = 20
idade_maior = 30
if idade >= idade_limite and idade<= idade_maior:
    print(f'{nome} Pode pegar o imprestimo cara, liberado !')
else:
    print(f'{nome} Cara vc não pode, sinto muito.')