from Repository.CashRepostitory import CashRepository


class CashService:

    def __init__(self):
        self._cashRepository = CashRepository()

    def money(self):
        return self._cashRepository.money()
