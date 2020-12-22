usuario = input('Nome de user:')
senha = input('Senha de user:')

usuario_db = 'cassio luciano da silva'
senha_bd = '123456'

if usuario_db == usuario and senha_bd == senha:
    print('Voce está logado')
else:
    print('Usuario Ou senha invalida')