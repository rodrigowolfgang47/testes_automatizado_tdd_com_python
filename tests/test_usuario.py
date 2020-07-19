from leilao.dominio import Usuario, Leilao
from leilao.tests.excecoes import LanceInvalido
import pytest


@pytest.fixture
def rodrigo():
    return Usuario('Rodrigo', 100)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_verificar_se_apos_o_usuario_dar_o_lance_o_valor_da_carteira_eh_subitraido(rodrigo, leilao):
    rodrigo.propor_lance(leilao, 50.0)

    assert rodrigo.carteira == 50.0

def test_deve_verificar_se_o_usuario_pode_dar_um_lance_igual_o_valor_da_carteira(rodrigo, leilao):
    rodrigo.propor_lance(leilao, 100)

    assert rodrigo.carteira == 0.0

def test_deve_verificar_se_o_usuario_nao_pode_dar_um_lance_maior_que_o_valor_da_carteira(rodrigo, leilao):

    with pytest.raises(LanceInvalido):

        rodrigo.propor_lance(leilao, 200)

        assert rodrigo.carteira == 100