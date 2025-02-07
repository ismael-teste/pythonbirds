
"""
Criar uma classe caroo que vai possuir dois atributos compostos por outras
duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado a velocidade
2) Metodo acelerar, que devera incrementar a velocidade em uma unidade
3) Metodo frear, que deverá decrementar a velocidade em duas unidades

A Direcao tera a responsabilidade de controlar a direcao. Ela oferece os
 seguintes atributos:

1) Valor de direcao com valores possiveis: Norte, Sul, Leste e Oeste
2) Metodo girar_a_direita
2) Metodo girar_a_esquerda

    Exemplo:
    >>> # testando o motor
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

    >>> # Testando direcao
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
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

from motor import Motor
from direcao import Direcao


class Carro:

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor


    def calcular_velocidade(self):
        return self.motor.velocidade


    def acelerar(self):
        return self.motor.acelerar()



    def frear(self):
        return self.motor.frear()



    def calcular_direcao(self):
        return self.direcao.valor


    def girar_a_direita(self):
        return self.direcao.girar_a_direita()


    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

if __name__ == "__main__":
    carro = Carro()
