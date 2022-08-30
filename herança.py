class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    def nome(self):
        return f'{self.__nome}'

class Cliente(Pessoa):
    def __init__(self, nome, cpf, limite):
        Pessoa.__init__(self, nome, cpf)
        self.__limite = limite
    def nome(self):
        return f'Nome: {self._Pessoa__nome} - limite: {self.__limite}'
class Funcionario(Pessoa):
    def __init__(self,nome, cpf, matricula):
        Pessoa.__init__(self, nome, cpf)
        self.__matricula = matricula



cliente1 = Cliente('Marco', '111.111.111-11',2000)
func1 = Funcionario('Juca silva sauro','888.999.666.54',81896)
print(cliente1.nome())
print(func1.nome())