from Domain.Movie import Movie
from Repository.MovieRepository import MovieRepository


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

    def alugar(self, cod: int):
        return self._movieRepository.alugar(cod)