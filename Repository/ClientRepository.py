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

    def update(self, client: Client):
        for item in self._clients:
            if item["CPF"] == client.getCPF():
                item["Name"] = client.getName()
                return "Cliente atualizado com sucesso."
        raise ValueError("Cliente não encontrado.")

