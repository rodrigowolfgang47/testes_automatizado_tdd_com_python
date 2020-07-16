from unittest import TestCase
from leilao.dominio import Usuario, Leilao, Lance, Avaliador

class TestAvaliador(TestCase):

    def setUp(self):
        self.rodrigo = Usuario("rodrigo")
        self.lance_rodrigo = Lance(self.rodrigo, 100)
        self.leilao = Leilao('Cavaco do Nicolau Maquiavel')
        self.leilao.lances.append(self.lance_rodrigo)


    def test_deve_retornar_o_menor_e_maior_valor_quando_instanciado_de_forma_crescente(self):
        pablo = Usuario('pablo')
        lance_pablo = Lance(pablo, 150)

        self.leilao.lances.append(lance_pablo)

        avaliador = Avaliador()

        avaliador.avalia_lance(self.leilao)

        valor_esperado_maior = 150
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, avaliador.maior_lance)
        self.assertEqual(valor_esperado_menor, avaliador.menor_lance)

    def test_deve_retornar_o_menor_e_maior_valor_quando_instanciado_de_forma_decrescente(self):

        pablo = Usuario('pablo')

        lance_pablo = Lance(pablo, 90)

        self.leilao.lances.append(lance_pablo)

        avaliador = Avaliador()

        avaliador.avalia_lance(self.leilao)

        valor_esperado_maior = 100
        valor_esperado_menor = 90

        self.assertEqual(valor_esperado_maior, avaliador.maior_lance)
        self.assertEqual(valor_esperado_menor, avaliador.menor_lance)

    def test_deve_retornar_como_menor_e_como_o_mesmo_quando_houver_so_um_lance(self):

        avaliador = Avaliador()

        avaliador.avalia_lance(self.leilao)

        self.assertEqual(100, avaliador.maior_lance)
        self.assertEqual(100, avaliador.menor_lance)

    def test_deve_retornar_o_menor_e_maior_valor_quando_forem_adicionados_mais_de_dois_lances_de_forma_crescente(self):
        pablo = Usuario('Pablo')
        clovis = Usuario('Clovis')

        lance_pablo = Lance(pablo.nome, 150)
        lance_clovis = Lance(clovis, 200)

        self.leilao.lances.append(lance_pablo)
        self.leilao.lances.append(lance_clovis)

        avaliador = Avaliador()

        avaliador.avalia_lance(self.leilao)

        valor_esperado_maior = 200
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, avaliador.maior_lance)
        self.assertEqual(valor_esperado_menor, avaliador.menor_lance)