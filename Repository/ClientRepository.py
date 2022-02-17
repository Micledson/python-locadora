from Domain.Client import Client


class ClientRepository:
    _clients = []

    def save(self, client: Client):
        self._clients.append({"Name": client.getName(), "CPF": client.getCPF()})
        print("Cliente cadastrado com sucesso.")

