from unittest import TestCase
from leilao.dominio import Usuario, Leilao, Lance
class TestAvaliador(TestCase):

    def setUp(self):
        self.rodrigo = Usuario("rodrigo")
        self.lance_rodrigo = Lance(self.rodrigo, 100)
        self.leilao = Leilao('Cavaco do Nicolau Maquiavel')
        self.leilao.propoe(self.lance_rodrigo)


    def test_deve_retornar_o_menor_e_maior_valor_quando_instanciado_de_forma_crescente(self):
        pablo = Usuario('pablo')
        lance_pablo = Lance(pablo, 150)

        self.leilao.propoe(lance_pablo)

        valor_esperado_maior = 150
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)
        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)

    def test_deve_retornar_o_menor_e_maior_valor_quando_instanciado_de_forma_decrescente(self):

        pablo = Usuario('pablo')

        lance_pablo = Lance(pablo, 90)

        self.leilao.propoe(lance_pablo)

        valor_esperado_maior = 100
        valor_esperado_menor = 90

        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)
        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)

    def test_deve_retornar_como_menor_e_como_o_mesmo_quando_houver_so_um_lance(self):

        self.assertEqual(100, self.leilao.maior_lance)
        self.assertEqual(100, self.leilao.menor_lance)

    def test_deve_retornar_o_menor_e_maior_valor_quando_forem_adicionados_mais_de_dois_lances_de_forma_crescente(self):
        pablo = Usuario('Pablo')
        clovis = Usuario('Clovis')

        lance_pablo = Lance(pablo.nome, 150)
        lance_clovis = Lance(clovis, 200)

        self.leilao.propoe(lance_pablo)
        self.leilao.propoe(lance_clovis)

        valor_esperado_maior = 200
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)
        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)