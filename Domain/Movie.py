class Movie:
    def __init__(self, cod: int, name: str, price: float, quantity: int):
        self._cod = cod
        self._name = name
        self._price = price
        self._quantity = quantity

    def getName(self) -> str:
        return self._name

    def getCOD(self) -> int:
        return self._cod

    def getPrice(self) -> float:
        return self._price

    def getQuantity(self) -> int:
        return self._quantity
