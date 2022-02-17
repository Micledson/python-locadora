from Domain.Client import Client


class ClientRepository:
    _clients = []

    def save(self, client: Client):
        self._clients.append({"Name": client.getName(), "CPF": client.getCPF()})
        print("Cliente cadastrado com sucesso.")

    def clients(self):
        return self._clients

    def client(self, cpf: int):
        for client in self._clients:
            if client["CPF"] == cpf:
                return client
        raise ValueError("Cliente não encontrado.")

