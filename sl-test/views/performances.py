
from views.dashboard import Dashboard as dn
import timeit, gc, sys

import streamlit as st
import matplotlib.pyplot as plt

class Performances :

    @classmethod
    def test_dashboard(cls, filename):
        all_movies = dn.init_data(filename)
        all_movies.get_short_list(5)

        dn.init_hist_realyse_years(all_movies)
        dn.show_pie_ratings(all_movies)

        return all_movies

    @classmethod
    def show(cls, filename) :
        st.title("Mesures de performances")

        sl.write(cls.execution_time(filename))
        st.pyplot(cls.repeat_time(filename))
        sl.write(cls.sizeofblocks(filename))

        


        
    @classmethod
    def execution_time(cls, filename) :
        # temps d'éxécution
        n = 20

        result = timeit.timeit(lambda:Performances.test_dashboard(filename), number = n, globals = globals())
        time = result / n * 1000    

        return f" temps de charge et de traitement des données : {time : .2f} s"

    @classmethod
    def repeat_time(cls, filename):
        # temps d'éxécution
        n = 20
        r = 3

        results = timeit.repeat(lambda:Performances.test_dashboard(filename), number = n, repeat = r, globals = globals())

        st.title("Execution times")
        fig, ax = plt.subplots()
        ax.hist(results)

        return fig

    @classmethod
    def sizeofblocks(cls, filename):
        gc.collect()
        before = sys.getallocatedblocks()
        
        movies = cls.test_dashboard(filename)
        
        tot = sys.getallocatedblocks() - before

        message = "Espace mémoire " + str(tot) + " octets."
        
        message  += " taille de la data en mémoire : " + str(sys.getsizeof(movies)))

        return message
