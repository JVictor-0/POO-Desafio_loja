from Loja import Compra, Cliente, Vendedor
import datetime


def main():

    Pedro = Vendedor('Pedro', 21, 900)
    Fernando = Cliente('Fernando', 17)

    compra1 = Compra(Pedro, datetime.now(), 400)

    Fernando.registrar_compra(compra1)

    print(f'')
