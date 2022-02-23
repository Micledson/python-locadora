from Utils.JsonManager import JsonManager


class CashRepository:

    def __init__(self):
        self._jsonPath = "/Data/CashRegister.json"
        self._jsonManager = JsonManager()

    def save(self, money: float, quantity: int):
        print("Deu R${}".format((money * quantity)))

        value: float = self._jsonManager.open(self._jsonPath, {"Money": 0.0})

        newValue = value["Money"] + float(money * quantity)

        data = {"Money": newValue}
        self._jsonManager.update(self._jsonPath, data)

    def money(self):
        return self._jsonManager.open(self._jsonPath, {"Money": 0.0})
