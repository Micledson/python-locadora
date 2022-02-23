from Options.ClientOptions import ClientOptions
from Options.MovieOptions import MovieOptions
from Options.CashOptions import CashOptions


class Options:
    def __init__(self):
        self._loop()

    def _loop(self):
        while True:
            print("1 - Cliente\n2 - Filme\n3 - Caixa\n0 - Sair")
            choice = int(input())

            if choice == 0:
                break
            elif choice == 1:
                self._loadClientOptions()
            elif choice == 2:
                self._loadMovieOptions()
            elif choice == 3:
                self._loadCashOptions()

    def _loadClientOptions(self):
        clientOptions = ClientOptions()

    def _loadMovieOptions(self):
        movieOptions = MovieOptions()

    def _loadCashOptions(self):
        cashOptions = CashOptions()
