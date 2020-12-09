nome = 'Cassio luciano da silva' #String
idade = 32 #int
altura = 1.68 #double
peso = 75 #int
data_inicial = '20/09/1988' #String

#formula imc peso dividido pelo quadrodo da altura 

massa_corporal = peso / (altura** 2 )

print('Meu nome é ',nome,'Tenho ',idade ,'Anos Minha altura',altura,' Data de nascimento',data_inicial, 'Meu imc é =',massa_corporal )

print('Nome : ',nome)
print('idade : ',idade)
print('Altura : ',altura)
print('Peso :',peso)
print("Data nascimento",data_inicial)

#função format

print( 'Meu nome é {} Eu tenho {} anos, tenho {} de altura, Acho que tenho {} kg, nascimento em {}, O calculo do meu Meu IMC'.format(nome,idade,altura,peso,data_inicial,massa_corporal))

#aqui eu consigo repetir a quantidade de repetiçoes 
print( 'Meu nome é  {0} {0} {0} {0} Eu tenho {1} '.format(nome,idade,))

#Melhor forma de se fazer

print (f'meu nome é {nome} tenho {idade}, a minha altura é {altura}, Acho que meu pes é {peso} e o calculo do IMC É {massa_corporal}')

minhamenssagemtodaaqui = f''' 
Meu nome é {nome}
Idade = {idade}
altura = {altura}
peso = {peso}
O calculo do seu IMC É = {massa_corporal}
''' 
print(minhamenssagemtodaaqui)

#dessa forma vai retornar um valor booleano
valorbooleano = 10<0
print(valorbooleano)
input()