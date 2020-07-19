import sys


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
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.menor_lance = sys.float_info.max
        self.maior_lance = sys.float_info.min
        self.__lances = []

    def __str__(self):
        for lance in self.lances:
            return f'lances do {lance.usuario.nome} foi de {lance.valor}'

    def propoe(self, lance: Lance):

        if not self.lances or self.lances[-1].usuario != lance.usuario and lance.valor > self.lances[-1].valor:
            self.__lances.append(lance)
            for lance in self.lances:
                if lance.valor > self.maior_lance:
                    self.maior_lance = lance.valor

                if lance.valor < self.menor_lance:
                    self.menor_lance = lance.valor
        else:
            raise ValueError('Lance invalido')

    @property
    def lances(self):
        return self.__lances[:]

