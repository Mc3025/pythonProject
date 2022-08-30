class Carro:
    def __init__(self, nome, marca, ano, velocidade):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, acelerar):
        self.velocidade = self.velocidade + acelerar
        print(f'Velocidade atual acelerando: {self.velocidade}')
        if self.velocidade > 110:
            print(f'Multa! {self.velocidade} Km/h')
            return

    def freiar(self, freiar):
        self.velocidade = self.velocidade - freiar
        print(f'velocidade atual freiando: {self.velocidade}')

