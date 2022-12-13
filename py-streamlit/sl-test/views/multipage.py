"""
Ce module contient la classe MultiPage qui permet de générer une applicatin Streamlit multi-pages à partir de classes d'objets. 
"""

import streamlit as st

class MultiPage: 

    def __init__(self) -> None:
        """
        __init__ constructeur qui initialise la liste de pages
        """
        self.pages = []
    
    def home_title(self) :
        """
        home_title Titre principale de la home page
        """
        st.title("App Dashboard Netflix")

    def add_page(self, title, obj) -> None: 
        """ ajout d'une page dans la liste de pages, sous la forme d'un couple titre + classe
        Args:
            title ([str]): titre de la page à afficher dans le menu
            
            obj : classe python qui contient toutes les méthodes d'une page Streamlit
        """

        self.pages.append({  
                "title": title, 
                "object": obj
            })

    def run(self, md):
        """
            génère le menu sous la forme d'une sidebar et traite les sélections pour ouvrir les pages correspondantes.

            md([str]) : chemin du fichier de données
        """ 
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        # show the page

        page["object"].show(md)