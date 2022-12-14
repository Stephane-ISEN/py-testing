# Tests de performances

Nous allons ajouter une page à notre appli qui affiche des métriques de performances.

## Ajout de la nouvelle page

en vous inspirant du fichier `dashboard.py` ajouter un fichier `performances.py` dans le répertoire `views`. Il contient la classe de même nom, qui permet de construire la page de performances, et contient la méthode de classe show() qui affiche tout simplement le titre "mesure de performances" sur la page Streamlit.

Pour que la nouvelle page s'affiche dans l'appli web, il faut modifier le constructeur de la classe Home. Le code suivant ajoute la page dashboard au menu :
`wapp.add_page("Dashboard Netflix", Dashboard)`

Faites de même pour la page performances.

Vous pouvez tester l'affichage de la nouvelle page dans votre navigateur.

## Premier test

Nous voulons mesurer les performances de la construction de la page Dashboard. Il nous faut donc exécuter tout le code de la page. Nous allons écrire une nouvelle méthode de classe dans Performances :

      @classmethod
      def test_dashboard(cls, filename):
        all_movies = dn.init_data(filename)
        all_movies.get_short_list(5)
        
        dn.init_hist_realyse_years(all_movies)
        dn.show_pie_ratings(all_movies)
        
        return all_movies

`dn`est un objet de type Dashboard, il faut penser à importer le code.

Le premier test constitue à mesurer le temps d'éxécution du traitement. Pour ça, nous allons utiliser la méthode `timeit`de la librairie du même nom : [timeit](https://docs.python.org/fr/3/library/timeit.html)

      @classmethod
      def execution_time(cls, filename) :
              # temps d'éxécution
              n = 20
              
              result = timeit.timeit(lambda:Performances.test_dashboard(filename), number = n, globals = globals())
              time = result / n * 1000    
              
              st.write(f" temps de charge et de traitement des données : {time : .2f} ms")

Il ne vous reste plus qu'à faire appel à cette méthode dans le `show()` de votre classe Performances.
