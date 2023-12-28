import streamlit as st
import numpy as np
import joblib
import pandas as pd

st.title('AUS Rainfall Prediction')

pipeline_entrenado1 = joblib.load('C:/Users/eugen/OneDrive\Desktop/app_streamlit/RainfallTomorrowAUS.joblib')
pipeline_entrenado2 = joblib.load('C:/Users/eugen/OneDrive\Desktop/app_streamlit/RainTomorrowAUS.joblib')

MinTemp = st.slider('MinTemp (°C)', -10.0, 50.0, 0.0)
MaxTemp = st.slider('MaxTemp (°C)', -10.0, 50.0, 0.0)
Rainfall = st.slider('Rainfall (mm)', 0.0, 400.0, 0.0)
Evaporation = st.slider('Evaporation (mm)', 0.0, 200.0, 0.0)
Sunshine = st.slider('Sunshine (h)', 0.0, 24.0, 0.0)
WindGustDir = st.slider('WindGustDir',1, 16, 8)
WindGustSpeed = st.slider('WindGustSpeed (km/h)', 0.0, 200.0, 0.0)
WindDir9am = st.slider('WindDir9am',1, 16, 8)
WindDir3pm = st.slider('WindDir3pm',1, 16, 8)
WindSpeed9am = st.slider('WindSpeed9am (km/h)', 0.0, 200.0, 0.0)
WindSpeed3pm = st.slider('WindSpeed3pm (km/h)', 0.0, 200.0, 0.0)
Humidity9am = st.slider('Humidity9am (%)', 0.0, 100.0, 0.0)
Humidity3pm = st.slider('Humidity3pm (%)', 0.0, 100.0, 0.0)
Pressure3pm = st.slider('Pressure3pm (hPa)', 870.0, 1080.0, 1000.0)
Cloud9am = st.slider('Cloud9am', 0, 8, 0)
Cloud3pm = st.slider('Cloud3pm', 0, 8, 0)
RainToday = st.slider('RainToday',0 , 1 , 0)

# Diccionario de puntos cardinales y su codificación
puntos_cardinales = {'N': 1, 'NE': 2, 'NW': 3, 'NNE': 4, 'NNW': 5,
                     'S': 6, 'SE': 7, 'SW': 8, 'SSE': 9, 'SSW': 10,
                     'W': 11, 'WNW': 12, 'WSW': 13, 'E': 14, 'ENE': 15, 'ESE': 16}


# Mostrar puntos cardinales y su codificación
st.header("Puntos Cardinales y Codificación:")
columnas = st.columns(3)  # Divido en 3 columnas

for cardinal, codificacion in puntos_cardinales.items():
    with columnas[codificacion % 3]:
        st.text(f"{cardinal}: {codificacion}")

data_para_predecir = np.array([[MinTemp, 
                                MaxTemp, 
                                Rainfall, 
                                Evaporation, 
                                Sunshine, 
                                WindGustDir, 
                                WindGustSpeed, 
                                WindDir9am, 
                                WindDir3pm, 
                                WindSpeed9am, 
                                WindSpeed3pm, 
                                Humidity9am, 
                                Humidity3pm, 
                                Pressure3pm,
                                Cloud9am,
                                Cloud3pm,
                                RainToday]])

prediccionRainfall = pipeline_entrenado1.predict(data_para_predecir)
prediccionRain = pipeline_entrenado2.predict(data_para_predecir)

# Display de predicciones
st.header("Predicted Rainfall")
st.write(prediccionRainfall)
st.header("Predicted Rain (0: No / 1: Yes)")
st.write(prediccionRain)

