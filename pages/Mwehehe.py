
import streamlit as st
import os
from PIL import Image
st.markdown("<h1 style='text-align: center; color: white;'>The Gallery of Isha <3</h1>", unsafe_allow_html=True)

image_folder = "Assets/Photos"
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    img = Image.open(image_path)
    st.image(img, caption="I love you", use_column_width=True)

