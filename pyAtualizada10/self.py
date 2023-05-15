class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprime_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa = Pessoa("Ana", 30)
pessoa.imprime_informacoes() # output: "Nome: Ana", "Idade: 30"
