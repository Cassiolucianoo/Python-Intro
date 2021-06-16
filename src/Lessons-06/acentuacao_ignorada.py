import unidecode
palavra = "prógrãmação"
palavraSemAcentuacao = unidecode.unidecode(palavra)
print(palavraSemAcentuacao)

if(palavraSemAcentuacao.find('cao')):
  print("Encontrado!")