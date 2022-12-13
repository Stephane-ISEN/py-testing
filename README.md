# py-testing

Projet de dashboard à destination des tests.

## architecture

Toute l'appli est codé en objet, architecture qui rend plus simple les tests, en plus de rendre le code évolutif.
- **data** : contients les fichiers csv de données.
- **models** : contients 2 classes permettant de traiter les données.
- **views** : contient tous le code générant l'appli streamlit.
- **app.py** : lance l'appli stremalit directement à partir de ce fichier Python.

## la docstring

Outils et normes pour les commentaires du code. voir les ressources suivantes :
- un petit tuto sur la docstring avec VS Code : https://www.docstring.fr/formations/documenter-son-code/les-differents-types-de-commentaires-201/
- des exemples de commentaires : https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e 

Le docstring bien faite permet, grâce à pydoc, de générer les aides contextuelles et la documentation html.

## exercice sur la docstring

en s'inspirant de ce qui a été fait sur la classe Movie, commentez la classe MoviesData.

le page de documentation html a été obtenue grâce à la commande suivante : `python -m pydoc -w movie`
