class Carro:

    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def chama_modelo(self):
        print("O modelo do carro é {}".format(self.modelo))



