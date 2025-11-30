import streamlit as st
import protly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualization")

# Generate same data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# plot data
fig, ax = plt.subplots()
ax.plot(x, y)
# Dismplay the plot
st.pyplot(fig)
