from leilao.dominio import Usuario, Leilao, Lance

rodrigo = Usuario("rodrigo")
pablo = Usuario('pablo')
lance_pablo = Lance(pablo.nome, 100)
lance_rodrigo = Lance(rodrigo.nome, 150)
leilao = Leilao('Celular')

leilao.propoe(lance_pablo)
leilao.propoe(lance_rodrigo)

for lance in leilao.lances:
    print(f"O Lance do usurário {lance.usuario.nome} deu um lance no valor de {lance.valor}")

print(f"O maior lance foi {leilao.menor_lance} e o menor lance foi de {leilao.menor_lance}")


