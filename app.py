import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
    page_title = "Titanic data",
    layout= 'wide',
    page_icon= ':cat:'

)

st.title("Titanic people data")

st.text("This dataset is the passenger information of Taitanic. The web page has a filter to age range, and visulizes the age distribution data.")


low, high = st.slider(
    'Select a age range of people',
    0, 80, (15, 35))
st.write('Values:', low, high)


url = "https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv"
titanic = pd.read_csv(url)

st.dataframe(titanic[(titanic['age'] >= low) & (titanic['age'] <= high)])

df = titanic.copy()

# create bins

df['bin'] = pd.cut(df['age'], bins=list(range(0, 86, 5)))

# summarize the data
summary = df['bin'].value_counts().sort_index()

# draw plot
plt.figure(figsize=(10, 6))
plt.bar(summary.index.astype(str), summary.values, color = "pink")
plt.xticks(rotation=45)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age distribution')

# 在Streamlit中显示图形
st.pyplot(plt)