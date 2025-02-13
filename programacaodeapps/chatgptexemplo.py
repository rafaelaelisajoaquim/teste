class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.altura += 0.5  # Cresce 0.5 cm se tiver menos de 21 anos
            self.idade += 1
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, cm):
        self.altura += cm
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Peso: {self.peso} kg, Altura: {self.altura} cm"

# Exemplo de uso:
pessoa = Pessoa("Carlos", 18, 70, 170)
print(pessoa)
pessoa.envelhecer(5)
print(pessoa)
pessoa.engordar(5)
print(pessoa)
pessoa.emagrecer(3)
print(pessoa)
pessoa.crescer(2)
print(pessoa)
