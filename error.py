# -*- coding: utf-8 -*-
"""error

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ztFroCJOkmPg_3VtGyCvXjuBeRbO15xe
"""


import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data for visualization
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [4, 6, 8, 2, 9]
})

# First visualization using Plotly Express
fig1 = px.bar(data, x='Category', y='Values', title='Bar Chart')

# Second visualization using Plotly Express
fig2 = px.pie(data, names='Category', values='Values', title='Pie Chart')

# Streamlit app
st.title('Streamlit App with Plotly Visualizations')

# Display the first visualization
st.plotly_chart(fig1)

# Display the second visualization
st.plotly_chart(fig2)
