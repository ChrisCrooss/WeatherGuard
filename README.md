# 🌦️ WeatherGuard
WeatherGuard is a multilingual, weather-aware safety companion designed for outdoor workers. By combining real-time weather data, job-specific health risk analysis, and AI-generated safety advice, WeatherGuard aims to reduce weather-related risks and promote informed decision-making in the field.
# Problem Statement
Outdoor workers face unpredictable and often dangerous weather conditions. Whether it's extreme heat, cold, wind, or rain, these environments pose serious health risks—particularly for workers in construction, agriculture, delivery, and gardening. Many lack access to real-time, localized guidance tailored to their job and climate.
# Our Solution
WeatherGuard combines:

Real-time weather data (via OpenWeatherMap)

AI-driven safety advice (via OpenAI GPT-4o)

Job-specific risk assessments and safety checklists

Multilingual UI support (English, Español, Français, Deutsch)

Interactive location mapping (via Folium)

This tool empowers outdoor workers with personalized, actionable health and safety information based on their current location and job type.

# Features
Enter your city and country code (e.g., Quito,EC)

Select your job type: Construction, Farming, Gardening, Delivery, Other

Get localized weather data: temperature, humidity, wind speed, conditions

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

# Clone the repository
git clone https://github.com/your-username/weatherguard.git
cd weatherguard

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

streamlit run app.py
Replace app.py with your script filename if different.

# API Keys
To run WeatherGuard, you’ll need:

OpenWeatherMap API key → Get one here

OpenAI API key → Get one here

Set them directly in the script or use environment variables for security:

bash
Copiar
Editar
export OPENAI_API_KEY='your-openai-key'
export WEATHER_API_KEY='your-openweather-key'
Or replace them in the code:

python
Copiar
Editar
openai.api_key = "sk-..."
api_key = "66ea..."
# Project Structure
bash
Copiar
Editar
weatherguard/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
# Intended Impact
WeatherGuard empowers outdoor workers to stay safe, proactive, and informed. By combining modern AI with real-time weather insights, it:

Reduces accidents and illnesses

Encourages preventative safety habits

Promotes language inclusivity in safety tech

Makes occupational health guidance accessible and interactive

# License
This project is licensed under the MIT License. See LICENSE for details.

# Acknowledgments
OpenWeatherMap for weather data

OpenAI for the GPT-4o language model

Streamlit for rapid UI development

Folium for mapping

# 🌐 Live Demo (Optional)
https://weatherguard.streamlit.app/
