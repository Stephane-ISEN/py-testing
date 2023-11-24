# Tests de performances

Nous allons ajouter une page à notre appli qui affiche des métriques de performances.

## Ajout de la nouvelle page

En vous inspirant du fichier `dashboard.py`, ajoutez un fichier `performances.py` dans le répertoire `views`. Il contient la classe du même nom, qui permet de construire la page de performances, et contient la méthode de classe `show()` qui affiche tout simplement le titre "Mesure de performances" sur la page Streamlit.

Pour que la nouvelle page s'affiche dans l'appli web, il faut modifier le constructeur de la classe Home. Le code suivant ajoute la page dashboard au menu :
`wapp.add_page("Dashboard Netflix", Dashboard)`

Faites de même pour la page performances.

Vous pouvez tester l'affichage de la nouvelle page dans votre navigateur.

## Premier test

Nous voulons mesurer les performances de la construction de la page Dashboard. Il nous faut donc exécuter tout le code de la page. Nous allons écrire une nouvelle méthode de classe dans `Performances` :

```
  @classmethod
  def test_dashboard(cls, filename):
    all_movies = dn.init_data(filename)
    all_movies.get_short_list(5)
    
    dn.init_hist_release_years(all_movies)
    dn.show_pie_ratings(all_movies)
    
    return all_movies

`dn` est un objet de type Dashboard, il faut penser à importer le code.

Le premier test consiste à mesurer le temps d'exécution du traitement. Pour ça, nous allons utiliser la méthode timeit de la librairie du même nom : [timeit](https://docs.python.org/fr/3/library/timeit.html)
```
  @classmethod
  def execution_time(cls, filename):
          # Temps d'exécution
          n = 20
          
          result = timeit.timeit(lambda:Performances.test_dashboard(filename), number = n, globals = globals())
          time = result / n * 1000    
          
          st.write(f"Temps de charge et de traitement des données : {time : .2f} ms")

Il ne vous reste plus qu'à faire appel à cette méthode dans le `show()` de votre classe Performances.

## Nouveau test de temps d'exécution

En vous inspirant de la fonction précédente, et en utilisant [repeat](https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat), affichez un histogramme qui présente plusieurs mesures du temps d'exécution.

## Mesure de la mémoire consommée

Grâce à la méthode suivante :
```
  @classmethod
  def sizeofblocks(cls, filename):
        gc.collect()
        before = sys.getallocatedblocks()
        
        movies = cls.test_dashboard(filename)
        
        tot = sys.getallocatedblocks() - before


*   **gc.collect()** : permet de nettoyer la mémoire,
*   **sys.getallocatedblocks()** : compte le nombre d'octets utilisés par l'appli (cf. [doc](https://docs.python.org/3/library/sys.html#sys.getallocatedblocks))

Comme pour les autres méthodes, pensez à l'appeler dans la méthode `show()`.

## Mesure des données en mémoire

Nous allons ajouter un dernier élément, la mesure de la mémoire utilisée par la donnée. Dans la méthode `sizeofblocks()`, utilisez la méthode `getsizeof()` pour afficher la taille mémoire des données utilisées pour le traitement.
