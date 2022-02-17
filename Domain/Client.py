class Client:
    def __init__(self, cpf: int, name):
        self._cpf = cpf
        self._name = name

    def getName(self):
        return self._name

    def getCPF(self):
        return self._cpf