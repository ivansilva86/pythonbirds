class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def class_metodo(cls):
        return f'{cls} - olhos {Pessoa.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    ivan = Mutante(nome='Ivan')
    luciano = Homem(ivan, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Carvalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(ivan.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(ivan.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(ivan.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.class_metodo(), luciano.class_metodo())
    pessoa = Pessoa('Anônima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(ivan, Pessoa))
    print(isinstance(ivan, Homem))
    print(ivan.olhos)
    print(luciano.cumprimentar())
    print(ivan.cumprimentar())

