import unidecode

palavras = [
  u"programação",
  u"acentuação",
  u"relação",
  u"será",
]
def to_ascii(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])
to_ascii(palavras)
print(palavras)