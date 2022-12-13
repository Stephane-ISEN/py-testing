import os
import pandas as pd
from models.movie import Movie

class MoviesData : 
    
    def __init__(self, file_name) :
        self.movies = []

        #ouverture du fichier
        path = os.getcwd()
        filename = os.path.join(path, file_name)

        dataset = pd.read_csv(filename)
        #nettoyage des données
        dataset2000 = dataset.dropna()
        dataset2000 = dataset2000.head(2000)

        for i in dataset2000.index :
            movie = Movie(dataset2000["show_id"][i], dataset2000["title"][i], dataset2000["release_year"][i], dataset2000["rating"][i])
            self.movies.append(movie)

    def get_short_list(self, size) :
        short_movies = self.movies[0:size]
        list_movies = []

        for movie in short_movies :
            list_movies.append(movie.get_tuple())

        return pd.DataFrame(list_movies) 

    def get_realyse_years_array(self):
        list_years = []

        for movie in self.movies :
            list_years.append(movie.realyse_year)
        
        return list_years


