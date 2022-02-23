from Handlers.CashHandler import CashHandler


class CashOptions:
    def __init__(self):
        self._cashHandler = CashHandler()

        self._options()

    def _options(self):
        print("1 - Exibir cash")
        choice = int(input())

        if choice == 1:
            self._cashHandler.money()