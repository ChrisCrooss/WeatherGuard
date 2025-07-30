# 🌦️ WeatherGuard
WeatherGuard is a multilingual, weather-aware safety companion designed for outdoor workers. By combining real-time weather data, job-specific health risk analysis, and AI-generated safety advices, WeatherGuard aims to reduce weather-related risks and foster informed decision-making in the field.
# Problem Statement
Outdoor workers face unknowed and often dangerous weather conditions. Whether it's extreme heat, cold, wind, or rain, these environments pose serious health risks—particularly for workers in construction, agriculture, delivery, and gardening. Many lack access to real-time, localized guidance tailored to their job and climate. Also the unaware of what they should do in each weather.
# Our Solution
WeatherGuard combines:

Real-time weather data (via OpenWeatherMap)

In process AI-driven safety advice (via OpenAI GPT-4o)

Job-specific risk assessments and safety checklists

Multilingual UI support (English, Español, Français, Deutsch)

Interactive location mapping (via Folium)

This tool will hellp outdoor workers with personalized and safety information based on their current location and job type. Algo giving precise information totally free.

# Features
Searcher by city (e.g., Quito,EC or Paris,FR)

Job type selector: Construction, Farming, Gardening, Delivery, Other

Get precise weather data: temperature, humidity, wind speed, conditions of the location previous searched

Receive health risk level classification: Low, Moderate, High, Extreme

Access custom safety checklists and tips based on weather + job

Ask the AI assistant for real-time advice in your language

View an interactive map showing your location

Submit user feedback to improve the tool

# Supported Languages
English

Español (Spanish)

Français (French)

Deutsch (German)

# Installation & Setup
Requirements
Python 3.8+

Streamlit

Folium

streamlit-folium

openai

requests

# Install dependencies
pip install -r requirements.txt

streamlit run app.py
Replace app.py with your script filename if different.

Also you can use run.bat after install requeriments.txt to run the app.

# API Keys

OpenWeatherMap API key

OpenAI API key

Set them directly in the script
# Intended Impact
WeatherGuard foster outdoor workers to stay safe, proactive, and informed. By combining modern AI with real-time weather insights, it:

Reduces accidents and illnesses by safety advices and precise information

Global information by the multilingual support

Makes personalized health guidance accessible and interactive with a checklist

# License
This project is licensed under the MIT License. See LICENSE for details.

# 🌐 Live Demo (Optional)
Tested in Google Chrome 
https://weatherguard.streamlit.app/
