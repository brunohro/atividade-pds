from pessoa import Pessoa

class Colaborador(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, matricula, carga_horaria):
        super().__init__(nome, idade, cpf, telefone)
        self.__matricula = matricula
        self.carga_horaria = carga_horaria
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
    
    def get_matricula(self):
        return self.__matricula