# PyTest
PyTest est un package qui permet de développer ses propres tests unitaires automatiques.

## Installation
`pip install pytest`

## Fonctionnement
Il faut tout d'abord créer un fichier `test_quelquechose.py`.

Dans ce fichier, créez une classe `TestClass` par classe à tester.
Y ajouter une méthode `test_methode(self)` par méthode à tester. L'idée est d'avoir une méthode de test par méthode à tester.
Écrire le code de test et ajouter autant de `assert` qu'il y a de méthodes pour valider la méthode à tester. 

Une fois le fichier de tests écrit, lancez la commande `pytest` dans la console.

Il y a un exemple dans le projet, fichier *test_netflix.py*, que vous pouvez exécuter avec la commande `pytest`.

## Exercice 1 : Tester MultiPage
Dans le fichier `test_netflix.py`, ajoutez une classe `TestMultiPage` qui a pour attribut `MP`, un objet de type `MultiPage` : 

`
  MP = MultiPage()
`

Attention à bien importer le fichier contenant la classe `MultiPage`.

Complétez la classe par les 3 méthodes suivantes :

```
class TestMultiPage :
  MP = MultiPage()

  def test_constructeur(self):
    # teste le constructeur
    # en vérifiant que MP est bien une instance de MultiPage
    pass
    
  def test_pages(self) :
    # teste l'attribut pages
    # en vérifiant qu'on a bien une liste de taille 0

  def test_add_pages(self) :
    # teste la méthode add_pages()
    # en ajoutant des pages 
    # en vérifiant la taille de pages
    # en vérifiant le format des pages ajoutées


On ne peut pas tester les méthodes home_title() et run() qui font appel à Streamlit pour afficher des composants graphiques sur une page web. Ça ne passe, évidemment pas, dans une console.

### test_constructeur
Pour ce test, on va tout simplement utiliser la méthode isinstance() pour vérifier que l'attribut MP est bien de type MultiPage :

```
  def test_constructeur(self):
    # teste le constructeur
    assert isinstance(self.MP, MultiPage)

`assert` permet de prendre le test en compte par pytest.

### test_pages
Ce test est simple aussi, puisqu'il doit vérifier l'existence de l'attribut `pages` dans `MP`. À la création de l'objet, cette liste est vide, donc de taille 0.

  def test_pages(self) :
    # teste l'attribut pages
    assert len(self.MP.pages) == 0

    ### test_add_pages
    Ce test doit vérifier que l'ajout de pages fonctionne bien. Le code commence donc par l'ajout de 2 pages et un nouveau test de la taille de l'attribut `pages`, qui doit être de 2, à ce moment. Puisque la liste `pages` attend des dictionnaires contenant un titre, en chaîne de caractères

  def test_add_pages(self) :
    # teste la méthode add_pages()
    self.MP.add_page("one", TestMultiPage)
    self.MP.add_page("two", TestMultiPage)
    
    assert len(self.MP.pages) == 2
    assert self.MP.pages[0]["title"] == "one"
    assert self.MP.pages[0]["object"] == TestMultiPage

## Exercice 2 : Tester MoviesData
Vous allez ajouter la classe `TestMoviesData`, toujours dans le fichier `test_netflix.py`, pour tester `MoviesData`.

Cette classe a un attribut, `MD` par exemple, qui est de type `MoviesData`. Il prend en paramètre le chemin de `netflix_test.csv` qui contient des données de tests.

La classe contient les méthodes suivantes :
*   **test\_constructeur()** : qui vérifie que la liste `movies` (attribut de `MD`) contient bien 3 éléments et que les 4 valeurs du premier (soit les 4 attributs de l'objet `Movie` : `title`, `id`, `release_year` et `rating`).
*   **test\_get\_short\_list()** : qui vérifie si la taille du dataframe retourné par la méthode `get_short_list(1)` est correcte et qu'un élément du dataframe a bien les données attendues. Le code de cette méthode est donné ci-dessous.
*   **test\_get\_release\_year\_array()** : qui vérifie que la liste retournée par la méthode `get_release_year_array()` contient bien les éléments suivants : 1993, 2021, 2021.

  def test_getShortList(self):
    short_list = self.MD.get_short_list(1)
    movie01 = pd.DataFrame([("s8", "Sankofa", 1993, "TV-MA")])
    
    assert len(short_list) == 1
    assert short_list.iloc[0,0] == movie01.iloc[0,0]
    assert short_list.iloc[0,1] == movie01.iloc[0,1]
    assert short_list.iloc[0,2] == movie01.iloc[0,2]
    assert short_list.iloc[0,3] == movie01.iloc[0,3]

