from Domain.Movie import Movie
from Services.MovieService import MovieService


class MovieHandler:
    def __init__(self):
        self._movieService = MovieService()

    def save(self):
        cod = int(input("Digite o código do filme: "))
        name = input("Digite o nome do filme: ")
        price = float(input("Digite o preço do filme: "))
        quantity = int(input("Digita a quantidade de copias: "))

        movie = Movie(cod, name, price, quantity)

        self._movieService.save(movie)

    def movies(self):
        movies = self._movieService.movies()
        for movie in movies:
            print("Filme: {} COD: {} Preço: {} Quantidade: {}"
                  .format(movie["Name"], movie["COD"], movie["Price"], movie["Quantity"]))

    def movie(self):
        cod = int(input("Digite o código do filme: "))
        try:
            movie = self._movieService.movie(cod)
            print("Filme: {} COD: {} Preço: {} Quantidade: {}"
                  .format(movie["Name"], movie["COD"], movie["Price"], movie["Quantity"]))
        except ValueError as err:
            print(err)

    def update(self):
        cod = int(input("Digite o código do filme: "))
        name = input("Digite o nome do filme: ")
        price = float(input("Digite o preço do filme: "))
        quantity = int(input("Digita a quantidade de copias: "))

        movie = Movie(cod, name, price, quantity)

        try:
            print(self._movieService.update(movie))
        except ValueError as err:
            print(err)

    def delete(self):
        cod = int(input("Digite o código do filme: "))

        try:
            print(self._movieService.delete(cod))
        except ValueError as err:
            print(err)

    def alugar(self):
        # rent
        cpf = int(input("Digite os números do CPF: "))
        cod = int(input("Digite o código do filme: "))
        quantity = int(input("Digite quantas cópias vai alugar: "))

        try:
            self._movieService.alugar(cpf, cod, quantity)
        except ValueError as err:
            print(err)

    def devolver(self):

        cpf = int(input("Digite os números do CPF: "))
        cod = int(input("Digite o código do filme: "))
        quantity = int(input("Digite quantas cópias vai alugar: "))

        try:
            self._movieService.devolver(cpf, cod, quantity)
        except ValueError as err:
            print(err)

    def currentlyRentedMovies(self):
        movies = self._movieService.currentlyRentedMovies()
        for movie in movies:
            print("Filme: {} COD: {} Preço: {} Quantidade: {} Cliente: {}"
                  .format(movie["Name"], movie["COD"], movie["Price"], movie["Quantity"], movie["Client"]))