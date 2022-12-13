from views.multipage import MultiPage
from views.dashboard import Dashboard

class Home :
    def __init__(self) -> None:

        # Create an instance of the web app 
        wapp = MultiPage()

        # Title of the home page
        wapp.home_title()

        # Add all your applications (pages) here
        wapp.add_page("Dashboard Netflix", Dashboard)

        # The main app
        wapp.run("py-streamlit/sl-test/data/netflix_titles.csv")

# instance of object for run the web app
home = Home()

