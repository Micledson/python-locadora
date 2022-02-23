from Services.CashService import CashService


class CashHandler:
    def __init__(self):
        self._cashService = CashService()

    def money(self):
        money = self._cashService.money()
        print("Tem R${} no Caixa.".format(money["Money"]))
