from Domain.Client import Client
from Repository.ClientRepository import ClientRepository


class ClientService:
    def __init__(self):
        self._clientRepository = ClientRepository()

    def save(self, client: Client):
        self._clientRepository.save(client)
