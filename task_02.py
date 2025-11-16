class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"


add_comedy = Comedy()
print(add_comedy.add_movie('Большой куш'))
add_drama = Drama()
print(add_drama.add_movie('Оружейный барон'))
