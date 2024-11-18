import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS
def local_css():
    st.markdown("""
    <style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f4f6f9;
    }
    .main-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .sidebar {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stSlider > div > div {
        background-color: #e1e8f0;
        border-radius: 8px;
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

# Load dataset
df = pd.read_csv('rainfall_dataset.csv')

# Main app
def main():
    # Apply custom CSS
    local_css()

    # Page configuration
    st.set_page_config(page_title='Rainfall Prediction Dashboard', layout='wide')

    # Title
    st.title('🌧️ Rainfall Prediction Dashboard')

    # Sidebar inputs for filtering data
    st.sidebar.header('Filter Data')
    
    temperature_filter = st.sidebar.slider('Temperature (°C)', min_value=int(df['temperature'].min()), 
                                            max_value=int(df['temperature'].max()), value=(int(df['temperature'].min()), int(df['temperature'].max())))
    
    humidity_filter = st.sidebar.slider('Humidity (%)', min_value=int(df['humidity'].min()), 
                                        max_value=int(df['humidity'].max()), value=(int(df['humidity'].min()), int(df['humidity'].max())))

    filtered_data = df[(df['temperature'] >= temperature_filter[0]) & (df['temperature'] <= temperature_filter[1]) &
                       (df['humidity'] >= humidity_filter[0]) & (df['humidity'] <= humidity_filter[1])]

    # Display filtered data
    st.subheader('Filtered Weather Data')
    st.dataframe(filtered_data)

    # Visualize Temperature vs Rainfall
    st.subheader('Temperature vs Rainfall')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_data['temperature'], filtered_data['rainfall'], color='orange')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('Temperature vs Rainfall')
    ax.grid(True)
    st.pyplot(fig)

    # Visualize Humidity vs Rainfall
    st.subheader('Humidity vs Rainfall')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_data['humidity'], filtered_data['rainfall'], color='green')
    ax.set_xlabel('Humidity (%)')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('Humidity vs Rainfall')
    ax.grid(True)
    st.pyplot(fig)

if __name__ == '__main__':
    main()
