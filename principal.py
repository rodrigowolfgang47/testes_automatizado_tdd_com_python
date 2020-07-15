from leilao.dominio import Usuario, Leilao, Lance, Avaliador

rodrigo = Usuario("rodrigo")
pablo = Usuario('pablo')

lance_pablo = Lance(pablo.nome, 100)
lance_rodrigo = Lance(rodrigo.nome, 150)

leilao = Leilao('Celular')

leilao.lances.append(lance_pablo)
leilao.lances.append(lance_rodrigo)

avaliador = Avaliador()

avaliador.avalia_lance(leilao)

for lance in leilao.lances:
    print(f"O Lance do usurário {lance.usuario} deu um lance no valor de {lance.valor}")

print(f"O maior lance foi {avaliador.maior_lance} e o menor lance foi de {avaliador.menor_lance}")


