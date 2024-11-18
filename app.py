import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Page configuration should be the first command
st.set_page_config(
    page_title='Rainfall Prediction', 
    page_icon='🌧️', 
    layout='wide'
)

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
    
    .prediction-result {
        background-color: #e8f4f8;
        border-left: 5px solid #3498db;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
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

# Load model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('rainfall_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

# Main application
def main():
    # Apply custom CSS
    local_css()
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="title">🌧️ Intelligent Rainfall Prediction System</h1>', unsafe_allow_html=True)
    
    # Load model
    model, scaler = load_model()
    
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
        
        # Input sliders with improved styling
        temperature = st.slider('Temperature (°C)', 
                                min_value=-10.0, 
                                max_value=50.0, 
                                value=25.0,
                                help="Select current temperature")
        
        humidity = st.slider('Humidity (%)', 
                             min_value=0, 
                             max_value=100, 
                             value=70,
                             help="Select current humidity level")
        
        wind_speed = st.slider('Wind Speed (km/h)', 
                               min_value=0.0, 
                               max_value=100.0, 
                               value=10.0,
                               help="Select current wind speed")
        
        pressure = st.slider('Pressure (hPa)', 
                             min_value=900, 
                             max_value=1100, 
                             value=1013,
                             help="Select current atmospheric pressure")
        
        # Prediction button
        predict_button = st.button('Predict Rainfall')
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Prediction section
    if predict_button:
        # Prepare input data
        input_data = [[temperature, humidity, wind_speed, pressure]]
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)[0]
        
        # Display prediction with enhanced styling
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
