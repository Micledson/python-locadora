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

    def clients(self):
        clients = self._clientService.clients()
        for client in clients:
            print("Cliente: {} CPF: {}".format(client["Name"], client["CPF"]))

    def client(self):
        cpf = int(input("Digite os números do CPF: "))
        try:
            client = self._clientService.client(cpf)
            print("Cliente: {} CPF: {}".format(client["Name"], client["CPF"]))
        except ValueError as err:
            print(err)

    def update(self):
        cpf = int(input("Digite os números do CPF: "))
        name = input("Digite o novo nome do cliente: ")

        client = Client(cpf, name)

        try:
            print(self._clientService.update(client))
        except ValueError as err:
            print(err)

