from Options.ClientOptions import ClientOptions


class Options:
    def __init__(self):
        self._loop()

    def _loop(self):
        while True:
            print("1 - Cliente\n0 - Sair")
            choice = int(input())

            if choice == 0:
                break
            elif choice == 1:
                self._loadClientOptions()

    def _loadClientOptions(self):
        clientOptions = ClientOptions()