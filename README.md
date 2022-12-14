# Un peu de TDD

Si on reprend le besoin du client, on voit qu'il manque un élément : le camembert.

Voici les 2 dbb qui définissent ce qu'il faut faire :

*Etant donné que l'utilisateur veut visionner un camembert du nombre des titres par classification
quand il est sur la page du Dashboard
Alors la page affiche un graphique de type camembert, avec autant de portions qu'il y a de classification
Et un titre pour ce graphique*

*Etant donné que l'appli doit calculer le nombre de titres par classification
quand elle génère le camembert
alors il faut une matrice de nombres de titres par classification
qui est obtenue à partir des objets titre*

Si on veut appliquer la méthode TDD, il faut : 
- coder un test qui plante,
- coder la fonction qui permet de valider le test.

## Le test
Le test est écrit dans le fichier `test_netflix.py`, dans la classe `TestMoviesData`. C'est en effet dans la classe `MoviesData`, qu'on va ajouter une méthode qui valide la 2e DBB. La méthode `get_rating_counts()` retourne une matrice contenant les données nécessaires à la construction du camembert. Cette matrice est obtenue à partir de la liste d'objet `movies`.

commencer par écrire un `test_get_rating_counts(self)` qui permet de valider que la fonction `get_rating_counts()` retourne la matrice suivante : 

**  TV-MA   1  
    TV-14   1  
    PG-13   1**  

si vous utiliser la commande `pytest`ce test doit être rouge, pour le moment.

Ecrire la fonction `get_rating_counts()` qui permet de passer le test au vert

## le camembert avec Streamlit
En vous inspirant de ce qui a été fait pour l'histogramme, ajouter la méthode `show_pie_rating()` dans la classe `Dashboard` et mettez à jour la méthode `show()`.

Vous pouvez tester en affichant votre page Streamlit dans le navigateur.
