class Veiculo:
       
    contador = 1

    def __init__(self, marca, modelo, placa, ano, preco):
        self.id = Veiculo.contador
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.preco = preco
        Veiculo.contador += 1

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "placa": self.placa,
            "ano": self.ano,
            "preco": self.preco,
        }