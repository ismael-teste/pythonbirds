class Direcao:

    def __init__(self):
        self.valor = "Norte"


    def girar_a_direita(self):
        if self.valor == "Norte":
            self.valor = "Leste"
        elif self.valor == "Leste":
            self.valor = "Sul"
        elif self.valor == "Sul":
            self.valor = "Oeste"
        else:
            self.valor = "Norte"


    def girar_a_esquerda(self):
        if self.valor == "Norte":
            self.valor = "Oeste"
        elif self.valor == "Oeste":
            self.valor = "Sul"
        elif self.valor == "Sul":
            self.valor = "Leste"
        else:
            self.valor = "Norte"

if __name__ == "__main__":
    direc = Direcao()
    print(direc.valor)
    direc.girar_a_diretira()
    print(direc.valor)
    direc.girar_a_diretira()
    print(direc.valor)
    direc.girar_a_diretira()
    print(direc.valor)
