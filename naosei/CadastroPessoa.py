
class CadastroPessoas:
    def __init__(self):
        self.pessoas=[]

    def adicionarPessoas(self, nome, idade, cpf):
        pessoa = {"Nome": nome, "Idade": idade, "CPF": cpf}
        self.pessoas.append(pessoa)
    def apagarPessoas(self):
        self.pessoas=[]