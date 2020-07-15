from unittest import TestCase


class TestAvaliador(TestCase):
    def test_avalia_lance(self):
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

        valor_esperado_maior = 150
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, avaliador.maior_lance)
        self.assertEqual(valor_esperado_menor, avaliador.menor_lance)

class TestAvaliador2(TestCase):
    def test_avalia_lance(self):
        from leilao.dominio import Usuario, Leilao, Lance, Avaliador

        rodrigo = Usuario("rodrigo")
        pablo = Usuario('pablo')

        lance_rodrigo = Lance(rodrigo.nome, 150)
        lance_pablo = Lance(pablo.nome, 100)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_pablo)
        leilao.lances.append(lance_rodrigo)

        avaliador = Avaliador()

        avaliador.avalia_lance(leilao)

        valor_esperado_maior = 150
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, avaliador.maior_lance)
        self.assertEqual(valor_esperado_menor, avaliador.menor_lance)
