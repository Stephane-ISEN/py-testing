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
`
  MP = MultiPage()
`

Attention à bien importer le fichier contenant la classe `MultiPage`.

compléter la classe par les 3 méthodes suivantes :

    class TestMultiPage :
      MP = MultiPage()
    
      def test_constructeur(self):
        # test le constructeur
        # en vérifiant que MP est bien une instance de MultiPage
        pass
        
      def test_pages(self) :
        # test l'attribut pages
        # en vérifiant qu'on a bien une liste de taille 0
    
      def test_add_pages(self) :
        # test la méthode add_pages()
        # en ajoutant des pages 
        # en vérifiant la taille de pages
        # en vérifiant le format des pages ajouter

On ne peut pas tester les méthodes home_title() et run() qui font appel à Streamlit pour afficher des composants graphiques sur une page web. Ca ne passe, évidement pas, dans une console.

### test_constructeur
Pour ce test, on va tout simplement utiliser la méthode isinstance() pour vérifier que l'attribut MP est bien de type MultiPage :

      def test_constructeur(self):
        # test le constructeur
        assert isinstance(self.MP, MultiPage)

`assert`permet de prendre le test en compte par pytest.

### test_pages
Ce test est simple aussi, puisqu'il doit vérifier l'existence de l'attribut `pages`dans `MP`. A la création de l'objet, cette liste est vide, donc de taille 0.

      def test_pages(self) :
        # test l'attribut pages
        assert len(self.MP.pages) == 0

### test_add_pages
Ce test doit vérifier que l'ajout de pages fonctionne bien. Le code commence donc par l'ajout de 2 pages et un nouveau test de la taille de l'attribut `pages`, qui doit être de 2, à ce moment.
Puisque la liste `pages` attend des dictionnaires contenant un titre, en chaine de caractère, et une classe d'objet, le test va vérifier les types d'une des pages ajoutées dans la liste.

      def test_add_pages(self) :
        # test la méthode add_pages()
        self.MP.add_page("one", TestMultipage)
        self.MP.add_page("two", TestMultipage)
        
        assert len(self.MP.pages) == 2
        assert self.MP.pages[0]["title"] == "one"
        assert self.MP.pages[0]["object"] == TestMultipage 

    


