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

class TestMoviesData :
    MD = MoviesData("data/netflix_test.csv")

    def test_constructeur(self):
        assert len(self.MD.movies) == 3

        movie01 = self.MD.movies[0]

        assert movie01.title == "Sankofa"
        assert movie01.id == "s8"
        assert movie01.realyse_year == 1993
        assert movie01.rating == "TV-MA"

    def test_getShortList(self):
        short_list = self.MD.get_short_list(1)
        movie01 = pd.DataFrame([("s8", "Sankofa", 1993, "TV-MA")])

        assert len(short_list) == 1
        assert short_list.iloc[0,0] == movie01.iloc[0,0]
        assert short_list.iloc[0,1] == movie01.iloc[0,1]
        assert short_list.iloc[0,2] == movie01.iloc[0,2]
        assert short_list.iloc[0,3] == movie01.iloc[0,3]

    def test_get_realyse_years_array(self):
        years = self.MD.get_realyse_years_array()
        
        assert years == [1993, 2021, 2021]

    def test_get_rating_counts(self):
        ratings = self.MD.get_rating_counts()
        ratings2 = pd.Index(["TV-MA","TV-14","PG-13"]).value_counts()
        print("matrice : " + str(ratings))
        assert ratings.get("TV-MA") == ratings2.get("TV-MA")
        assert ratings.get("TV-14") == ratings2.get("TV-14")
        assert ratings.get("PG-13") == ratings2.get("PG-13")

class TestMultipage :

    MP = MultiPage()

    def test_constructeur(self):

        assert isinstance(self.MP, MultiPage) 
    
    def test_pages(self):
        assert len(self.MP.pages) == 0

    def test_add_page(self) :
        self.MP.add_page("one", TestMultipage)
        self.MP.add_page("two", TestMultipage)

        assert len(self.MP.pages) == 2
        assert self.MP.pages[0]["title"] == "one"
        assert self.MP.pages[0]["object"] == TestMultipage 
