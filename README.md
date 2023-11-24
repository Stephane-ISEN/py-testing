# py-testing

Projet de dashboard à destination des tests.

## Architecture

Toute l'application est codée en objet, architecture qui rend plus simples les tests, en plus de rendre le code évolutif.
- **data** : contient les fichiers CSV de données.
- **models** : contient 2 classes permettant de traiter les données.
- **views** : contient tout le code générant l'application Streamlit.
- **app.py** : lance l'application Streamlit directement à partir de ce fichier Python.

## La docstring

Outils et normes pour les commentaires du code. Voir les ressources suivantes :
- Un petit tuto sur la docstring avec VS Code : https://www.docstring.fr/formations/documenter-son-code/les-differents-types-de-commentaires-201/
- Des exemples de commentaires : https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e 

La docstring bien faite permet, grâce à pydoc, de générer les aides contextuelles et la documentation HTML.

## Exercice sur la docstring

En s'inspirant de ce qui a été fait sur la classe Movie, commentez la classe MoviesData.

La page de documentation HTML a été obtenue grâce à la commande suivante : `python -m pydoc -w movie`
