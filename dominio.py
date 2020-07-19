from leilao.tests.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def propor_lance(self, leilao, valor):
        if self._valor_eh_valido(valor):
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self.__carteira -= valor
        else:
            raise LanceInvalido('valor indisponível na carteira')

    def _valor_eh_valido(self, valor):
        return valor <= self.carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_lance = 0
        self.maior_lance = 0

    def __str__(self):
        for lance in self.lances:
            return f'lances do {lance.usuario.nome} foi de {lance.valor}'

    def propoe(self, lance: Lance):

        if self._lance_valido(lance):
            if not self._tem_lance():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lance(self):
        return self.__lances

    def _usuarios_sao_diferentes(self, lance):
        if self.lances[-1].usuario != lance.usuario:
            return True
        else:
         raise LanceInvalido('O mesmo usuario não pode dar dois lances seguidos')

    def _valor_maior_que_o_anterior(self, lance):
       if lance.valor > self.lances[-1].valor:
           return True
       else:
           raise LanceInvalido("O lance não pode ser menor que o ultimo lance")

    def _lance_valido(self, lance):
        return not self._tem_lance() or self._usuarios_sao_diferentes(lance) and self._valor_maior_que_o_anterior(lance)
