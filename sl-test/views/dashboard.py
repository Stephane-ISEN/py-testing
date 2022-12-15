from models.movies_data import MoviesData

import streamlit as st
import matplotlib.pyplot as plt

class Dashboard:
    """
     Classe static qui créée la page web Dashboard grâce à Streamlit

    """
    @classmethod
    def init_data(cls, filename) :
        """
        init_data initialise les données des titres à parti d'un fichier csv

        Args:
            filename (str): nom du fichier csv à importer

        Returns:
            MoviesData: objet qui contient une collection de titre et les méthodes pour les manipuler
        """
        return MoviesData(filename)

    @classmethod
    def init_hist_realyse_years(cls, movies) :
        """
        init_hist_realyse_years prépare un histogramme, pour les années de réalisation, grâce à pyplot

        Args:
            movies (MoviesData): objet contenant les données pour l'histogramme

        Returns:
            Figure: figure piplot de l'histogramme
        """
        fig, ax = plt.subplots()
        ax.hist(movies.get_realyse_years_array())

        return fig

    @classmethod
    def show_pie_ratings(cls, movies) :
        """
        show_pie_ratings prépare un camembert grâce à piplot

        Args:
            movies (_type_): objet contenant les données pour le camembert

        Returns:
            Figure: figure piplot du camembert
        """
        pie, ax2 = plt.subplots()
        ax2.pie(movies.get_rating_counts())

        return pie

    @classmethod
    def show(cls, filename):
        """
        show construction et affichage de la page grâce à Streamlit

        Args:
            filename ([str]): chemin du fichier de données
        """
        all_movies = cls.init_data(filename)

        st.title("Netflix")
        st.write(all_movies.get_short_list(5))

        st.title("Realyse Years")
        fig = cls.init_hist_realyse_years(all_movies)
        st.pyplot(fig)

        st.title("Rating")
        pie = cls.show_pie_ratings(all_movies)
        st.pyplot(pie)
