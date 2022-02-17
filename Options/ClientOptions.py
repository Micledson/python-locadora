from Handlers.ClientHandler import ClientHandler


class ClientOptions:
    def __init__(self):
        self._clientHandler = ClientHandler()

        self._options()

    def _options(self):
        print("1 - Criar Cliente\n2 - Exibir Clientes\n3 - Buscar Cliente\n4 - Atualizar Cliente")
        choice = int(input())

        if choice == 1:
            self._clientHandler.save()
        elif choice == 2:
            self._clientHandler.clients()
        elif choice == 3:
            self._clientHandler.client()
        elif choice == 4:
            self._clientHandler.update()
