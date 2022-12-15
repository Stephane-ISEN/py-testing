import os
import streamlit.bootstrap as stb

if __name__ == "__main__":
    """
     lancement de Streamlit à partir d'un code Python
    """
    path = os.getcwd()
    filename = os.path.join(path, "py-streamlit/sl-test/views/home.py")
    
    stb.run(filename, '',[], flag_options=[])