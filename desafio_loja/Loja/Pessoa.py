class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'

    def is_adulto(self):
        return 'Adulto' if self.idade >= 18 else 'Menor de Idade'
