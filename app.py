import streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(
    page_title = "Titanic data",
    layout= 'wide',
    page_icon= ':cat:'

)

st.title("Titanic people data")

low, high = st.slider(
    'Select a age range of people',
    0, 80, (15, 35))
st.write('Values:', low, high)


url = "https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv"
titanic = pd.read_csv(url)

st.dataframe(titanic[(titanic['age'] >= low) & (titanic['age'] <= high)])

