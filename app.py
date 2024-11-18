import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration should be first
st.set_page_config(page_title='Rainfall Prediction Dashboard', layout='wide')

# Custom CSS
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
    }
    
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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

# Main application
def main():
    # Apply custom CSS
    local_css()
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="title">🌧️ Intelligent Rainfall Prediction System</h1>', unsafe_allow_html=True)
    
    # Create columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Weather Prediction Dashboard
        Use the sliders on the right to input current weather parameters 
        and predict expected rainfall.
        """)
    
    # Sidebar inputs
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.header('Weather Parameters')
        
        # Input sliders
        temperature = st.slider('Temperature (°C)', min_value=-10.0, max_value=50.0, value=25.0)
        humidity = st.slider('Humidity (%)', min_value=0, max_value=100, value=70)
        wind_speed = st.slider('Wind Speed (km/h)', min_value=0.0, max_value=100.0, value=10.0)
        pressure = st.slider('Pressure (hPa)', min_value=900, max_value=1100, value=1013)
        
        # Prediction button
        predict_button = st.button('Predict Rainfall')
        st.markdown('</div>', unsafe_allow_html=True)

    # Prediction section
    if predict_button:
        # Dummy prediction logic as model is removed
        prediction = temperature * 0.1 + humidity * 0.2  # Just a placeholder formula
        
        # Display prediction with styling
        st.markdown(f"""
        <div class="prediction-result">
            <h3>Prediction Result</h3>
            <p>Predicted Rainfall: <strong>{prediction:.2f} mm</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualization
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(['Predicted Rainfall'], [prediction], color='#3498db', alpha=0.7)
        ax.set_ylabel('Rainfall (mm)')
        ax.set_title('Rainfall Prediction Visualization')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
