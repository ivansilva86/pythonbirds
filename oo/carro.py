"""
Você deve criar uma classe carro que irá possuir dois atributos compostos por 2 outras classes:

1) Motor
2) Direcao

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado de velocidade
2) Método acelerar, que deverá incrementar a velocidade em 1 unidade
3) Método frear, que deverá decrementar a velocidade em 2 unidade

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor da direção com valores possíveis: Norte, Sul, Leste, Oeste
2) Método girar à direita
3) Método girar à esquerda

    Exemplo
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando a Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_a_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_a_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_a_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_a_velocidade()
    0
    >>> carro.calcular_a_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:

    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

    pass


class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

    pass




