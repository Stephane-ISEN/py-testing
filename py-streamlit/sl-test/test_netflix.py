from views.multipage import MultiPage
from models.movie import Movie
from models.movies_data import MoviesData

import pandas as pd

# pip install pytest
# le fichier doit s'appeller test_quelquechose.py
# les fonctions de test se nomme : test_mafonction()
# on utilise assert pour savoir si un test est bon ou pas
# commande pytest dans la console

class TestMovie :

    MOVIE = Movie("test01", "title", "2022", "rating")

    def test_constructeur(self):
        assert self.MOVIE.title == "title"
        assert self.MOVIE.id == "test01"
        assert self.MOVIE.realyse_year == "2022"
        assert self.MOVIE.rating == "rating"
    
    def test_get_tuple(self):
        assert self.MOVIE.get_tuple() == ( "test01", "title", "2022", "rating")

