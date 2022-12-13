
class Movie :
    """
     Classe Movie pour générer des objets contenants toutes les données d'un titre lu dans le csv
    """
    def __init__(self, id, title, realyse_year, rating):
        """
        __init__ constructeur qui initialise les attributs d'un objet de type Movie

        Args:
            id (str): id show du titre
            title (str): titre complet
            realyse_year (int): année de réalisation sur 4 caractères
            rating (str): catégorie du titre
        """
        self.id = id
        self.title = title
        self.realyse_year = realyse_year
        self.rating = rating

    def get_tuple(self) :
        """
        get_tuple retourne les données du titre sous forme d'un tuple

        Returns:
            _type_: tuple contenant toutes les données du titre
        """
        return (self.id, self.title, self.realyse_year, self.rating)


