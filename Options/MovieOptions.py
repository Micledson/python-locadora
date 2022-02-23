from Handlers.MovieHandler import MovieHandler


class MovieOptions:
    def __init__(self):
        self._movieHandler = MovieHandler()

        self._options()

    def _options(self):
        print("1 - Criar Filme\n2 - Exibir Filmes\n3 - Buscar Filme\n4 - Atualizar Filme\n"
              "5 - Deletar Filme\n6 - Alugar Filme\n7 - Devolver Filme\n8 - Filmes Atualmente Alugados")
        choice = int(input())

        if choice == 1:
            self._movieHandler.save()
        elif choice == 2:
            self._movieHandler.movies()
        elif choice == 3:
            self._movieHandler.movie()
        elif choice == 4:
            self._movieHandler.update()
        elif choice == 5:
            self._movieHandler.delete()
        elif choice == 6:
            self._movieHandler.alugar()
        elif choice == 7:
            self._movieHandler.devolver()
        elif choice == 8:
            self._movieHandler.currentlyRentedMovies()

