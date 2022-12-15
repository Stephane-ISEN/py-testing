import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

#ouverture du fichier
dataset = pd.read_csv("./data/netflix_titles.csv")
#nettoyage des données
dataset2000 = dataset.dropna()
dataset2000 = dataset2000.head(2000)

# affichage des premières données
st.title("Netflix")
st.write(dataset2000.head())

arr = dataset.release_year.array
fig, ax = plt.subplots()
ax.hist(arr)

st.pyplot(fig)


# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)

dataset.rating.value_counts()
data = pd.crosstab(dataset.rating, "freq") 
print(data)
cam, ax2 = plt.subplots()
ax2.pie(data)
ax2.axis("equal")

st.pyplot(cam)


