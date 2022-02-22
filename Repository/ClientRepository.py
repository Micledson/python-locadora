from Domain.Client import Client
from Utils.JsonManager import JsonManager


class ClientRepository:

    def __init__(self):
        self._jsonPath = "/Data/ClientData.json"
        self._jsonManager = JsonManager()

    def save(self, client: Client):
        clients = self._jsonManager.open(self._jsonPath)
        clients.append({"Name": client.getName(), "CPF": client.getCPF()})
        self._jsonManager.update(self._jsonPath, clients)

        print("Cliente cadastrado com sucesso.")

    def clients(self):
        clients = self._jsonManager.open(self._jsonPath)
        return clients

    def client(self, cpf: int):
        clients = self._jsonManager.open(self._jsonPath)
        for client in clients:
            if client["CPF"] == cpf:
                return client
        raise ValueError("Cliente não encontrado.")

    def update(self, client: Client):
        clients = self._jsonManager.open(self._jsonPath)
        for item in clients:
            if item["CPF"] == client.getCPF():
                item["Name"] = client.getName()
                self._jsonManager.update(self._jsonPath, clients)
                return "Cliente atualizado com sucesso."
        raise ValueError("Cliente não encontrado.")

    def delete(self, cpf: int):
        clients = self._jsonManager.open(self._jsonPath)
        for index in range(len(clients)):
            if clients[index]["CPF"] == cpf:
                clients.pop(index)
                self._jsonManager.update(self._jsonPath, clients)
                return "Cliente deletado."
        raise ValueError("Cliente não encontrado.")
