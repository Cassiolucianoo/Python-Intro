try:
    n_1 = int(input("Informe o primeiro numero : "))
    n_2 = int(input("Informe o próximo numero : "))

    soma = n_1 + n_2
    print ("{0} + {1} = {2}".format(n_1, n_2, soma))

    print("Entrada de dados corretas.")

except ValueError:
    print("Somente numeros sao aceitos. Tente novamente.")

input()