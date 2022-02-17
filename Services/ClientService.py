from Domain.Client import Client
from Repository.ClientRepository import ClientRepository


class ClientService:
    def __init__(self):
        self._clientRepository = ClientRepository()

    def save(self, client: Client):
        self._clientRepository.save(client)

    def clients(self):
        return self._clientRepository.clients()

    def client(self, cpf: int):
        return self._clientRepository.client(cpf)

    def update(self, client: Client):
        return self._clientRepository.update(client)

    def delete(self, cpf: int):
        return self._clientRepository.delete(cpf)