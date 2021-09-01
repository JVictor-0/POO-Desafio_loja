from Loja import Pessoa
import datetime


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)
        self.criacao = datetime.today()
        return compra

    def get_data_ultima_compra(self, data):
        self.data = data
        self.data = (datetime.today() - self.criacao).days
        return f'{self.data}'
#        return (self.data.strftime('%d/%m/%Y') )

    def total_compras(self):
        for compra in compras:
            print(compra)
