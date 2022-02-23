from Domain.Movie import Movie
from Repository.MovieRepository import MovieRepository
from Services.ClientService import ClientService


class MovieService:
    def __init__(self):
        self._movieRepository = MovieRepository()

    def save(self, movie: Movie):
        self._movieRepository.save(movie)

    def movies(self):
        return self._movieRepository.movies()

    def movie(self, cod: int):
        return self._movieRepository.movie(cod)

    def update(self, movie: Movie):
        return self._movieRepository.update(movie)

    def delete(self, cod: int):
        return self._movieRepository.delete(cod)

    def alugar(self, cpf: int, cod: int, quantity: int):

        try:
            clientService = ClientService()
            client = clientService.client(cpf)
            movie = self.movie(cod)
            if movie["Quantity"] >= quantity:
                return self._movieRepository.alugar(cpf, cod, quantity)
            else:
                print("Não temos tantas cópias disponíveis")
        except ValueError as err:
            print(err)

    def devolver(self, cpf: int, cod: int, quantity: int):
        try:
            clientService = ClientService()
            client = clientService.client(cpf)
            movie = self.movie(cod)
            if movie["Quantity"] <= quantity:
                return self._movieRepository.devolver(cpf, cod, quantity)
            else:
                print("Você está tentando devolver mais cópias que o necessário")
        except ValueError as err:
            print(err)

    def currentlyRentedMovies(self):
        return self._movieRepository.currentlyRentedMovies()