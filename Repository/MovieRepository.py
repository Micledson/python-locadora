from Domain.Movie import Movie
from Utils.JsonManager import JsonManager


class MovieRepository:

    def __init__(self):
        self._jsonPath = "/Data/MovieData.json"
        self._reportPath = "/Data/relatorio.json"
        self._jsonManager = JsonManager()

    def save(self, movie: Movie):
        movies = self._jsonManager.open(self._jsonPath)
        movies.append({"Name": movie.getName(), "COD": movie.getCOD(),
                       "Price": movie.getPrice(), "Quantity": movie.getQuantity()})
        self._jsonManager.update(self._jsonPath, movies)

        print("Cliente cadastrado com sucesso.")

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

    def alugar(self, cod: int):
        movies: Movie = self._jsonManager.open(self._jsonPath)
        for movie in movies:
            if movie["COD"] == cod:
                movie["Quantity"] -= 1
                self._jsonManager.update(self._jsonPath, movies)
                reports = self._jsonManager.open(self._reportPath)

                for report in reports:
                    if report["COD"] == cod:
                        report["Quantity"] += 1
                        self._jsonManager.update(self._reportPath, reports)
                        return movie

                reports.append({"Name": movie["Name"], "COD": movie["COD"],
                                "Price": movie["Price"], "Quantity": 1})
                self._jsonManager.update(self._reportPath, reports)
                return movies
        raise ValueError("Filme não encontrado.")
