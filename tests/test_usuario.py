from leilao.dominio import Usuario, Leilao

def test_deve_verificar_se_apos_o_usuario_dar_o_lance_o_valor_da_carteira_eh_subitraido():
    rodrigo = Usuario('Rodrigo', 100)
    leilao = Leilao('Celular')

    rodrigo.propor_lance(leilao, 50.0)

    assert rodrigo.carteira == 50.0