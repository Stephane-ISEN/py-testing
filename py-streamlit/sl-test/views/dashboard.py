from models.movies_data import MoviesData

import streamlit as st
import matplotlib.pyplot as plt

class Dashboard:
    @classmethod
    def init_data(cls, filename) :
        return MoviesData(filename)

    @classmethod
    def init_hist_realyse_years(cls, movies) :

        fig, ax = plt.subplots()
        ax.hist(movies.get_realyse_years_array())

        return fig

    @classmethod
    def show(cls, filename):
        
        all_movies = cls.init_data(filename)

        st.title("Netflix")
        st.write(all_movies.get_short_list(5))

        st.title("Realyse Years")
        fig = cls.init_hist_realyse_years(all_movies)
        st.pyplot(fig)

