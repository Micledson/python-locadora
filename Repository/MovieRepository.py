from Domain.Movie import Movie
from Repository.CashRepostitory import CashRepository
from Utils.JsonManager import JsonManager


class MovieRepository:

    def __init__(self):
        self._jsonPath = "/Data/MovieData.json"
        self._reportPath = "/Data/Report.json"
        self._jsonManager = JsonManager()

    def save(self, movie: Movie):
        movies = self._jsonManager.open(self._jsonPath)
        movies.append({"Name": movie.getName(), "COD": movie.getCOD(),
                       "Price": movie.getPrice(), "Quantity": movie.getQuantity()})
        self._jsonManager.update(self._jsonPath, movies)

        print("Filme cadastrado com sucesso.")

    def movies(self):
        movies = self._jsonManager.open(self._jsonPath)
        return movies

    def movie(self, cod: int):
        movies = self._jsonManager.open(self._jsonPath)
        for movie in movies:
            if movie["COD"] == cod:
                return movie
        raise ValueError("Filme não encontrado.")

    def update(self, movie: Movie):
        movies = self._jsonManager.open(self._jsonPath)
        for item in movies:
            if item["COD"] == movie.getCOD():
                item["Name"] = movie.getName()
                item["Price"] = movie.getPrice()
                item["Quantity"] = movie.getQuantity()
                self._jsonManager.update(self._jsonPath, movies)
                return "Filme atualizado com sucesso."
        raise ValueError("Filme não encontrado.")

    def delete(self, cod: int):
        movies = self._jsonManager.open(self._jsonPath)
        for index in range(len(movies)):
            if movies[index]["COD"] == cod:
                movies.pop(index)
                self._jsonManager.update(self._jsonPath, movies)
                return "Filme deletado."
        raise ValueError("Filme não encontrado.")

    def alugar(self, cpf: int, cod: int, quantity: int):
        movies: Movie = self._jsonManager.open(self._jsonPath)
        cashRepository = CashRepository()

        for movie in movies:
            if movie["COD"] == cod:
                movie["Quantity"] -= quantity
                self._jsonManager.update(self._jsonPath, movies)
                reports = self._jsonManager.open(self._reportPath)

                for report in reports:
                    if report["COD"] == cod and report["Client"] == cpf:
                        report["Quantity"] += quantity
                        cashRepository.save(movie["Price"], quantity)

                        self._jsonManager.update(self._reportPath, reports)
                        return movie

                reports.append({"Name": movie["Name"], "COD": movie["COD"], "Client": cpf,
                                "Price": movie["Price"], "Quantity": quantity})
                self._jsonManager.update(self._reportPath, reports)

                cashRepository.save(movie["Price"], quantity)

                return movies
        raise ValueError("Filme não encontrado.")

    def devolver(self, cpf: int, cod: int, quantity: int):
        movies: Movie = self._jsonManager.open(self._jsonPath)
        for movie in movies:
            if movie["COD"] == cod:

                reports = self._jsonManager.open(self._reportPath)

                for report in reports:
                    if report["COD"] == cod and report["Client"] == cpf:
                        movie["Quantity"] += quantity
                        self._jsonManager.update(self._jsonPath, movies)

                        report["Quantity"] -= quantity
                        self._jsonManager.update(self._reportPath, reports)
                        return movie

                return movies
        raise ValueError("Filme não encontrado.")

    def currentlyRentedMovies(self):
        return self._jsonManager.open(self._reportPath)
