class Pessoa():
    def __init__(self, nome, idade, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self._telefone = telefone

    def __str__(self):
        return self.nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        


