from unittest import TestCase
from leilao.dominio import Usuario, Leilao, Lance


class TestAvaliador(TestCase):

    def setUp(self):
        self.rodrigo = Usuario("rodrigo", 500)
        self.lance_rodrigo = Lance(self.rodrigo, 100)
        self.leilao = Leilao('Cavaco do Nicolau Maquiavel')
        self.leilao.propoe(self.lance_rodrigo)


    def test_deve_retornar_o_menor_e_maior_valor_quando_instanciado_de_forma_crescente(self):
        pablo = Usuario('pablo', 500)
        lance_pablo = Lance(pablo, 150)

        self.leilao.propoe(lance_pablo)

        valor_esperado_maior = 150
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)
        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)

    def test_nao_deve_permitir_dar_um_lance_menor_que_o_anterior(self):
        pablo = Usuario('pablo', 500)
        lance_pablo = Lance(pablo, 90)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_pablo)

    def test_deve_retornar_como_menor_e_como_o_mesmo_quando_houver_so_um_lance(self):

        self.assertEqual(100, self.leilao.maior_lance)
        self.assertEqual(100, self.leilao.menor_lance)

    def test_deve_retornar_o_menor_e_maior_valor_quando_forem_adicionados_mais_de_dois_lances_de_forma_crescente(self):
        pablo = Usuario('Pablo', 500)
        clovis = Usuario('Clovis', 500)

        lance_pablo = Lance(pablo.nome, 150)
        lance_clovis = Lance(clovis, 200)

        self.leilao.propoe(lance_pablo)
        self.leilao.propoe(lance_clovis)

        valor_esperado_maior = 200
        valor_esperado_menor = 100

        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)
        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)

    def test_usuario_nao_pode_dar_dois_laces_seguidos(self):

        pablo = Usuario("Pablo", 500)
        lance_pablo = Lance(pablo, 100)
        lance_pablo200 = Lance(pablo, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_pablo)
            self.leilao.propoe(lance_pablo200)

    def test_usuario_nao_pode_dar_dois_laces_seguidos_e_se_o_proximo_usuario_pode_dar_um_lance(self):

        pablo = Usuario("Pablo", 500)
        clovis = Usuario("clovis", 500)
        lance_pablo = Lance(pablo, 200)
        lance_pablo200 = Lance(pablo, 300)
        lance_clovis = Lance(clovis, 400)

        try:
            self.leilao.propoe(lance_pablo)
            self.leilao.propoe(lance_pablo200)
            self.fail(msg="Você não adicionou a excessão")

        except ValueError:
            self.leilao.propoe(lance_clovis)
            quantidade_de_lances = len(self.leilao.lances)
            valor_esperado_de_lances_na_lista = 3
            self.assertEqual(valor_esperado_de_lances_na_lista, quantidade_de_lances)