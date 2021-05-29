class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


    @staticmethod
    def metodo_estatico():
        return f"Metodo estatico"


    @classmethod
    def nome_atributos_classe(cls):
        return f"{cls} - olhos {cls.olhos}"



if __name__ == "__main__":
    ismael = Pessoa(nome='Ismael')
    luciano = Pessoa(ismael,  nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for f in luciano.filhos:
        print(f.nome)

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_atributos_classe(), luciano.nome_atributos_classe())
