from Handlers.ClientHandler import ClientHandler


class ClientOptions:
    def __init__(self):
        self._clientHandler = ClientHandler()

        self._options()

    def _options(self):
        print("1 - Criar Cliente")
        choice = int(input())

        if choice == 1:
            self._clientHandler.save()
