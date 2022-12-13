# PyTest

PyTest est un package qui permet de développer ses propres tests unitaires automatiques.

## installation
`pip install pytest`

## fonctionnement
Il faut tout d'abord créer une fichier test_quelquechose.py.

Dans ce fichier créer une classe TestClass par classe à tester.
Y ajouter une méthode test_methode(self) par méthode à tester. L'idée c'est d'avoir une méthode de test par méthode à tester.
Ecrire le code de test et ajouter autant de `assert` qu'il y a de méthode pour valider la méthode à tester. 

Une fois le fichier de tests écrit, lancer la commande `pytest`dans la console.

Il y a un exemple dans le projet, fichier *test_netflix.py* que vous pouvez éxécuter avec la commande `pytest`.

## exercice 1 : tester MultiPage

ajouter une class `TestMultiPage`qui a pour attribut MP, un objet de type MultiPage : 
  MP = MultiPage()

Attention à bien importer le fichier contenant la classe `MultiPage`.


