# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:06 2025

@author: BRYEMM004
"""

import streamlit as st
import pandas as pd
from PIL import Image


import streamlit as st
from PIL import Image

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Emmanuel Biryabarema"
field = "Bioinformatics"
institution = "University of Cape Town"

# Display the basic information
st.write(f"**Name:** {name}")
st.write(f"**Field:** {field}")
st.write(f"**Institution:** {institution}")

# Load the image
image_path = "0011_us.jpg"  # Your local image path
try:
    image = Image.open(image_path)
except FileNotFoundError:
    st.error(f"Image not found at the specified path: {image_path}")
    st.stop()

# Resize the image using thumbnail while keeping the aspect ratio
max_size = (100, 100)  # Max size for width and height
image.thumbnail(max_size)

# Display the resized image
st.image(image, caption="Profile Picture", use_column_width=False)


# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "emmanuelb060@gmail.com"
st.write(f"You can reach {name} at {email}.")
