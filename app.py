import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    .main-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .title {
        color: #2c3e50;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        margin-bottom: 20px;
        background: linear-gradient(90deg, #3498db, #2ecc71);
        padding: 10px;
        border-radius: 10px;
        color: white;
    }
    
    .title img {
        width: 50px;
        vertical-align: middle;
        margin-right: 10px;
    }
    
    .prediction-result {
        background-color: #e8f4f8;
        border-left: 5px solid #3498db;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }

    .stSlider > div > div {
        background-color: #ecf0f1;
        border-radius: 10px;
    }

    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Apply custom CSS
    local_css()
    
    # Page configuration
    st.set_page_config(page_title='Rainfall Prediction', page_icon='🌧️', layout='wide')
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Title with image
    st.markdown("""
    <h1 class="title">
        <img src="https://www.example.com/your-image.png" alt="Rainfall"> 
        🌧️ Intelligent Rainfall Prediction System
    </h1>
    """, unsafe_allow_html=True)
    
    # Your app's functionality goes here...

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

