from Domain.Client import Client
from Services.ClientService import ClientService


class ClientHandler:
    def __init__(self):
        self._clientService = ClientService()

    def save(self):
        name = input("Digite o nome do cliente: ")
        cpf = int(input("Digite os números do CPF: "))

        _client = Client(cpf, name)

        self._clientService.save(_client)

